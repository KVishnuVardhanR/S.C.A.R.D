import time
from cancer import cancer_detect
import logging as log
import numpy as np
from tkinter import filedialog
from gui import startpage, register, prediction, finished, additional_help, location
from googlesearch import search  
import webbrowser


startpage('Welcome To S.C.A.R.D')    

identity = register()   

def openfile():
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'Open file',
                                          filetypes = (('Image files', '*.jpg'), ('All files','*.*')))
    return filename


image_file = openfile()
    
skmodel = 'skin_cancer_detect/skin_cancer_detect'
device = 'CPU'

start_model_load_time = time.time()

#initailizing models 
sk_model = cancer_detect(skmodel, device)

#Loading models
sk_model.load_model()
total_model_load_time = time.time() - start_model_load_time

    
start_inference_time = time.time()
        

out = sk_model.predict(image_file)
   
total_time = time.time() - start_inference_time
total_inference_time = round(total_time, 1)

txt = '\n \n The probability of skin cancer\n is '+str(out*100)+'%.'


prediction(txt)

if identity == 1:
    y = additional_help()

    if y == 1:
        address = location()

        query = "skin cancer specialists in "+address+" practo"
          
        for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
            link = j
            break


        webbrowser.open(link)

    
    elif y == 2:
        # to search 
        query = "skin cancer forums"
          
        for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
            link = j
            break


        webbrowser.open(link)


finished()    

print("The total time to load the model is :"+str(total_model_load_time)+"sec")
print("The total inference time of the model is :"+str(total_inference_time)+"sec")      
