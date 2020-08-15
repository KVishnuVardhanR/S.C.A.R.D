from openvino.inference_engine import IENetwork, IECore
import cv2
import numpy as np
import logging as log

class cancer_detect:

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
        self.core = IECore()
        self.net = self.core.load_network(network=self.model, device_name=self.device,num_requests=1)

    def predict(self, image):
        try:
            image=cv2.imread(image)
            self.processed_image=self.preprocess_input(image)
            results= self.net.infer(inputs={self.input_name:self.processed_image})
            result = results[self.output_name]
            return result
        except Exception as e:
            log.error('Face detection failed, Could not detect any face in the frame')
            exit()


    def check_model(self):
        raise NotImplementedError

    def preprocess_input(self, image):
        self.image = cv2.resize(image, (224, 224))
        self.image = self.image.transpose((2,0,1))
        self.image = self.image.reshape(1, 3, 224, 224)
        return self.image

