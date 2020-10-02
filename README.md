# S.C.A.R.D
This project dubbed **S.C.A.R.D [Skin Cancer Detection At Edge for Real time Diagnostics]** intends in designing a **“Skin Cancer Detector with AI at Edge”**,  where it helps not only Doctors and Dermatologists to predict the probability of skin cancer, but also for the patients and to suggest remedies to prevent further damage, **connecting to forums for discussions and giving a smart search for skin specialists based on their geographic location with a very minimum hardware requirements**.

# Getting Started 
- Setup your local environment:
  - Download and install the **OpenVINO Toolkit**. The installations directions for OpenVINO can be found [here](https://docs.openvinotoolkit.org/latest/index.html)
  - Run the **Verification Scripts to verify your installation**. This is a very important step to be done before you proceed further.
- The project directory is structured as follows:
```
					project
					|
					|_ skin_cancer_detect
					|  
					|_ resources
					|  |_download.ico
					|  |_Reducing_the_Risk_of_Skin_Cancer.pdf
					|  |_images.jpg
					|  |_scard.pptx
					|
					|_ test_images
					|
					|_ README.md    
					|   
					|_ requirements.txt   
					|
					|_ LICENSE
					|
					|_ src
					   |_ main.py
					   |_ gui.py
					   |_ cancer.py
					   |_ Kaggle-Kernel-skin-cancer-detect.ipynb
	
```
  - The project directory contains a ```test_images``` folder which has 2 images **[Benign, Malignant]** can be used to test the model for predictions and to check their performances **i.e.;[Time take for Loading model, Time taken for performing inference and How accurate are the predictions]**.
  - It has ```requirements.txt``` file which contains all the necessary dependencies to be installed before running the project.
	
**Note: This project has been tested only in Windows 10 Operating System environment with Intel core i3-7100 processor which has an Intel Integrated GPU HD Graphics 630.**  


## Demo

- First, initialize the OpenVINO environment:
  - Open command prompt and cd to ```cd C:\Program Files (x86)\IntelSWTools\openvino\bin```
  - type ```setupvars.bat``` command and press *Enter* to initialize OpenVINO environment.
- Next, ```cd``` to the project directory:
- Now, run the following command to run the application:
  - ```python src\main.py ```

## References
- The entire working demo of the project can be veiwed through this [link](https://youtu.be/L05lsLCLja8).
- The **Keras model** which has been trained and saved as **.h5 file** in the **Kaggle Kernel**  converted to
**TensorFlow Frozen inference gragh .pb file** is further converted to **IR [Intermediate Representation] format** using **OpenVINO** can be found [here](https://www.dlology.com/blog/how-to-run-keras-model-inference-x3-times-faster-with-cpu-and-intel-openvino-1/).     