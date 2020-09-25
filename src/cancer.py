from openvino.inference_engine import IENetwork, IECore
import cv2
import numpy as np
import logging as log

def snapshot():
    """
    This function opens the camera and when user presses "Space bar" it takes
    a snapshot of the user and when the user presses "Escape" it exits the
    function

    Returns: It returns the image path which has been taken by the user
    """
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "skin_lesion.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return img_name


class cancer_detect:
    '''
    This module is used to skin cnacer Detection Model in OpenVINO and loads
    the model in specified hardware device for inference. The inference is
    performed on input skin lesion and returns the probability of skin cancer on
    the input skin lesion.
    '''
    def __init__(self, model_name, device='CPU'):

        self.model_weights=model_name+'.bin'
        self.model_structure=model_name+'.xml'
        self.device=device
        

        try:
            self.model=IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Could not Initialise the network. Have you enterred the correct model path?")

        self.input_name=next(iter(self.model.inputs))
        self.input_shape=self.model.inputs[self.input_name].shape
        self.output_name=next(iter(self.model.outputs))
        self.output_shape=self.model.outputs[self.output_name].shape

    def load_model(self):
        """ loading the model on the specified hardware device."""
        self.core = IECore()
        self.net = self.core.load_network(network=self.model, device_name=self.device,num_requests=1)

    def predict(self, image):
        """
        It takes the image for preprocessing and sends it to model for predictions.
        These predictions are give us the probabilities of skin cancer,The
        probability of cancer on the skin lesion is returned
        """
        try:
            image=cv2.imread(image)
            self.processed_image=self.preprocess_input(image)
            results= self.net.infer(inputs={self.input_name:self.processed_image})
            result = results[self.output_name]
            return result[0][1]
        
        except Exception as e:
            log.error('skin detection failed, Could not detect any image of the skin lesion')
            exit()
    

    def preprocess_input(self, image):
        """
        The iput image has to undergo preprocessing steps brfore making predictions
        For more information please check the doucumentation on using OpenVINO
        openmodel zoo pre-trained models.
        """
        self.image = image / 255
        self.image = cv2.resize(self.image, (224, 224))
        self.image = self.image.transpose((2,0,1))
        self.image = self.image.reshape(1, 3, 224, 224)
        return self.image

