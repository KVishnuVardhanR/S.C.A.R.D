from cancer import cancer_detect
import time
import os
import cv2
import argparse
import sys
import logging as log


def main(args):
    skmodel = args.SK
    device = args.D
    video_file = args.V

    start_model_load_time = time.time()

    #initailizing models
    
    sk_model = cancer_detect(skmodel, device)
    # Loading models

    sk_model.load_model()
    total_model_load_time = time.time() - start_model_load_time

    
    start_inference_time = time.time()
        
    try:
        print(sk_model.predict(video_file))

        total_time = time.time() - start_inference_time
        total_inference_time = round(total_time, 1)

        print("The total time to load all the models is :"+str(total_model_load_time)+"sec")
        print("The total inference time of the models is :"+str(total_inference_time)+"sec")
        
    except Exception as e:
        print("Could not run Inference: ", e)



if __name__=='__main__':
    parser=argparse.ArgumentParser()
    
    parser.add_argument('-V', default=None,
                        help = "Input file, User can enter path of video file or enter cam for webcam.")
    
    parser.add_argument('-SK', required=True,
                        help = "Path to xml file of Face detection model.")
    
    parser.add_argument('-D', default='CPU',
                        help = "specifying device like CPU,GPU,VPU,FPGA to run inference.")
    
    args=parser.parse_args()
    main(args)
