import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os

NORM_FONT=('Verdana',20)

def startpage(text):
    """ This function is the Introductory window dialog """
    
    popup = tk.Tk()

    popup.iconbitmap(default='resources/download.ico')
    popup.geometry("500x500")
    popup.wm_title('S.C.A.R.D')
    
    canvas = Canvas(popup, height=400, width=500, bg = 'white')
    
    imag = Image.open("resources/images.jpg")
    imag = imag. resize((500, 450), Image. ANTIALIAS)
    image = ImageTk.PhotoImage(imag)
    canvas.create_image(250, 175, anchor=CENTER, image = image)
    
    label = tk.Label(popup, text=text, bg="white",fg="black",font = NORM_FONT)
    label.pack(side='top' , fill='x')
    
    canvas.pack(fill = 'x')

    B1 = ttk.Button(popup, text ='Lets get started',command = popup.destroy)

    B1.pack(side = tk.RIGHT, fill = 'y')
    
    popup.mainloop()


def register():
    """
    This function is the registration page which is used for identifcation of
    the user as patient or doctor

    Returns: It returns the identification of the user
    """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Registration form", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90,y=60)

    #this creates 'Label' widget for Fullname and uses place() method.
    label_1 =Label(root,text="Enter your FullName", width=20,font=("bold",10))
    label_1.place(x=80,y=130)

    #this will accept the input string text from the user.
    entry_1=Entry(root)
    entry_1.place(x=240,y=130)

    
    #this creates 'Label' widget for Identification and uses place() method.
    label_4 =Label(root,text="which one describes you?", width=20,font=("bold",10))
    label_4.place(x=70,y=230)


    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    def getval():
        global xval
        if var.get() == 1:
            xval = 1
        elif var.get() ==2:
            xval = 2
        
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Patient",padx= 5, variable= var, value=1).place(x=235,y=230)
    Radiobutton(root,text="Doctor",padx= 20, variable= var, value=2).place(x=325,y=230)

    #this creates button for submitting the details provides by the user
    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=380)
    
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)

    #this will run the mainloop.
    root.mainloop()
    return xval

def ask_for_input():
    """
    This function is used to ask the user abiut how to give the input, whether to upload or taking pic

    Returns: It returns the type the user wants to give the input
    """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget and uses place() method.
    label_0 =Label(root,text="Please provide an image for analysis", width=20,font=("bold",20))
    label_0.pack(side = 'top',fill = 'x')


    label_4 =Label(root,text="You can either Take a picture or Upload?", width=35,font=("bold",12))
    label_4.place(x=40,y=130)

    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    def getval():
        global xval
        if var.get() == 1:
            xval = 1
        elif var.get() ==2:
            xval = 2
            
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Take a picture",padx= 5, variable= var, value=1).place(x = 135, y = 200)
    Radiobutton(root,text="Upload from PC", variable= var, value=2).place(x = 325, y = 200)

    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=350)
    
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)
    
    root.mainloop()
    return xval


def openfile():
    """
    This function opens a dialog box asking to choose an image file from
    your pc.

    Returns: It returns the filename
    """
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'Open file',
                                          filetypes = (('Image files', '*.jpg'), ('All files','*.*')))
    return filename


def open_doc():
    """ This function opens the .pdf file """
    os.startfile('C:/Users/Vishnu_K/Documents/My_Projects/Py_Pojects/S.C.A.R.D/resources/Reducing_the_Risk_of_Skin_Cancer.pdf')

def prediction(text):
    """ This function displays the prediction of the model """
    
    kin = tk.Tk()

    kin.iconbitmap(default='resources/download.ico')
    kin.geometry("500x500")
    kin.wm_title('S.C.A.R.D')
    
    label1 = tk.Label(kin, text=text, bg="white", fg="black",font = NORM_FONT)
    label1.pack(fill = 'x')

    label2 = tk.Label(kin, text='\n\n\n\n\nClick \"Open remedies\" button to get the list of remedies \nto prevent further damage of skin cancer.', fg="black",font = ('Verdana',12))
    label2.pack(fill='x')
    
    B1 = ttk.Button(kin, text ='Next',command = kin.destroy)
    B1.pack(side = tk.BOTTOM)
        
    B2 = ttk.Button(kin, text ='Open Remedies',command = open_doc)

    B2.pack(side = tk.BOTTOM)
    
    kin.mainloop()
    
def finished():
    """ This function is the finished window dialog """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x250")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget and uses place() method.
    label_0 =Label(root,text="Thank you for using S.C.A.R.D", width=20,font=("bold",20))
    label_0.pack(side = 'top',fill = 'x')
    
    #this creates 'Label' widget and uses place() method.
    label_4 =Label(root,text="Wishing good health for you and your family!!", width=40,font=("bold",15))
    label_4.place(x=40,y=130)
    
    ttk.Button(root, text ='Exit',command = root.destroy).place(x=420,y=225)
    
    #this will run the mainloop.
    root.mainloop()


def continue_or_back():
    """
    This function will help the patient to explore other additional features 
    """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget and uses place() method.
    label_0 =Label(root,text="Thank you for using S.C.A.R.D", width=20,font=("bold",20))
    label_0.pack(side = 'top',fill = 'x')


    label_4 =Label(root,text="Do you want to go back?", width=20,font=("bold",20))
    label_4.place(x=40,y=130)

     #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    def getval():
        global xval
        if var.get() == 1:
            xval = 1
        elif var.get() ==2:
            xval = 2
            
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Yes",padx= 5, variable= var, value=1).place(x = 135, y = 200)
    Radiobutton(root,text="No", variable= var, value=2).place(x = 325, y = 200)

    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=350)
    
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)
    
    root.mainloop()
    return xval


def additional_help():
    """ This function helps the patients to get access to smart features """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget and uses place() method.
    label_0 =Label(root,text="Additional help", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90,y=60)
        
    #this creates 'Label' widget and uses place() method.
    label_4 =Label(root,text="Choose one of the following?", width=20,font=("bold",10))
    label_4.place(x=40,y=230)

        
    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    def getval():
        global xval
        if var.get() == 1:
            xval = 1
        elif var.get() ==2:
            xval = 2
            
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="search for skin specialist",padx= 5, variable= var, value=1).place(x = 135, y = 250)
    Radiobutton(root,text="connect to forums",padx= 20, variable= var, value=2).place(x = 325, y = 250)

    #this creates button for submitting the details provides by the user
    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=350)
        
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)

    #this will run the mainloop.
    root.mainloop()
    return xval


def location():
    """ This function is used to ask the patient's address location and returns it """
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget and uses place() method.
    label_0 =Label(root,text="Search for skin specialist", width=20,font=("bold",20))
    label_0.pack(side = 'top', fill ='x')

    #this creates 'Label' widget and uses place() method.
    label_1 =Label(root,text="Enter your Area", width=20,font=("bold",10))
    label_1.place(x=80,y=130)

    #this will accept the input string text from the user.
    entry_field_variable = tk.StringVar()
    entry_1=Entry(root, textvariable=entry_field_variable)
    entry_1.place(x=240,y=130)

            
    #this creates 'Label' widget for example and uses place() method.
    label_4 =Label(root,text="Ex: area = whitefield bangalore", width=40,font=("bold",10))
    label_4.place(x =80, y = 150)


    def getval():
        global xval
        xval = entry_1.get()
                
    #this creates button for submitting the details provides by the user
    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=380)
            
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)

    #this will run the mainloop.
    root.mainloop()
    return xval
            
