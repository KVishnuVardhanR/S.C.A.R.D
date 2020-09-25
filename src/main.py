import time
import cv2
from cancer import cancer_detect, snapshot
import logging as log
import numpy as np
from tkinter import filedialog
from gui import startpage, register, prediction, finished, ask_for_input
from gui import additional_help, location, continue_or_back, openfile
from googlesearch import search  
import webbrowser

# A welcome Dialog box 
startpage('Welcome To S.C.A.R.D')    

# registration form for identification purposes
identity = register()   

# Ask for which way the user want to give input
input_way = ask_for_input()

if input_way == 1:
    # Get the file path of the image file
    image_file = snapshot()


elif input_way == 2:
    # Get the file path of the image file
    image_file = openfile()

try:
    # Cancer prediction model and default processor    
    skmodel = 'skin_cancer_detect/skin_cancer_detect'
    device = 'CPU'

    # starting model loading loading time 
    start_model_load_time = time.time()

    # initailizing models 
    sk_model = cancer_detect(skmodel, device)

    # Loading models
    sk_model.load_model()

    # counting time, taken to load the model
    total_model_load_time = time.time() - start_model_load_time

    # starting model inference time    
    start_inference_time = time.time()
            
    # perform inference inference on the given image and predict output 
    out = sk_model.predict(image_file)

    # counting time, taken to perform inference on the model   
    total_time = time.time() - start_inference_time
    total_inference_time = round(total_time, 1)

    txt = '\n \n The probability of skin cancer\n is '+str(out*100)+'%.'

    # A dialog box to view the predictions
    prediction(txt)

    # Enabling Smart features for the patient
    if identity == 1:

        # A while loop is used so that the user can explore both the options
        z = 1
        while z == 1:
                
            # A dialog box to choose a smart feature
            y = additional_help()
            if y == 1:
                
                # A dialog box to get the location of the patient
                address = location()

                # to search the query
                query = "skin cancer specialists in "+address+" practo"
                  
                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    link = j
                    break

                # opening the link in browser
                webbrowser.open(link)

            
            elif y == 2:
                 
                query = "skin cancer forums"
                  
                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    link = j
                    break

                webbrowser.open(link)

            z = continue_or_back()

            if z == 2:
                break

    # A Thank you dialog box
    finished()    

    # print the time taken by model to load and perform inference
    print("The total time to load the model is :"+str(total_model_load_time)+"sec")
    print("The total inference time of the model is :"+str(total_inference_time)+"sec")      

except Exception as e:
    log.error("Could not run Inference: ", e)
