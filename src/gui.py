import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os

NORM_FONT=('Verdana',20)

def startpage(text):                                                
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

    
    #this creates 'Label' widget for Gender and uses place() method.
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
    #B1.pack(side = tk.RIGHT)
    #this will run the mainloop.
    root.mainloop()
    return xval

def open_doc():
    os.startfile('C:/Users/Vishnu_K/Documents/My_Projects/Py_Pojects/skin_cancer_detection/resources/Reducing_the_Risk_of_Skin_Cancer.docx')

def prediction(text):                                                
    kin = tk.Tk()

    kin.iconbitmap(default='resources/download.ico')
    kin.geometry("500x500")
    kin.wm_title('S.C.A.R.D')
    
    #canvas = Canvas(kin, height=350, width=500, bg = 'white')
    
    #imag = Image.open(image_file)
    #imag = imag. resize((500, 450), Image. ANTIALIAS)
    #image = ImageTk.PhotoImage(imag)
    #canvas.create_image(250, 175, anchor=CENTER, image = image)
    
    label1 = tk.Label(kin, text=text, bg="white", fg="black",font = NORM_FONT)
    label1.pack()

    label2 = tk.Label(kin, text='\nClick Open remedies button to \nget the list of remedies \nto prevent further damage of\n skin cancer.', fg="black",font = NORM_FONT)
    label2.pack(fill='x')
    
    #canvas.pack(fill = 'x')
    
    B1 = ttk.Button(kin, text ='Next',command = kin.destroy)#.place(x=420,y=475)
    B1.pack(side = tk.BOTTOM)
        
    B2 = ttk.Button(kin, text ='Open Remedies',command = open_doc)#.place(x=420,y=475)

    B2.pack(side = tk.BOTTOM)
    
    kin.mainloop()
    
def finished():
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x250")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Thank you for using S.C.A.R.D", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.pack(side = 'top',fill = 'x')
    
    #this creates 'Label' widget for Gender and uses place() method.
    label_4 =Label(root,text="Wishing good health for you and your family!!", width=40,font=("bold",15))
    label_4.place(x=40,y=130)
    
    ttk.Button(root, text ='Exit',command = root.destroy).place(x=420,y=225)
    #B1.pack(side = tk.RIGHT)
    #this will run the mainloop.
    root.mainloop()

def additional_help():
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Additional help", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90,y=60)
        
    #this creates 'Label' widget for Gender and uses place() method.
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
        #B1.pack(side = tk.RIGHT)
        #this will run the mainloop.
    root.mainloop()
    return xval


def location():
    root = Tk()

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('S.C.A.R.D')
    root.iconbitmap(default='resources/download.ico')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Search for skin specialist", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.pack(side = 'top', fill ='x')

    #this creates 'Label' widget for Fullname and uses place() method.
    label_1 =Label(root,text="Enter your Area", width=20,font=("bold",10))
    label_1.place(x=80,y=130)

    #this will accept the input string text from the user.
    entry_field_variable = tk.StringVar()
    entry_1=Entry(root, textvariable=entry_field_variable)
    entry_1.place(x=240,y=130)

            
    #this creates 'Label' widget for Gender and uses place() method.
    label_4 =Label(root,text="Ex: area = whitefield bangalore", width=40,font=("bold",10))
    label_4.place(x =80, y = 150)


    def getval():
        global xval
        xval = entry_1.get()
                
    #this creates button for submitting the details provides by the user
    ttk.Button(root, text='Submit' , width=20, command = getval).place(x=180,y=380)
            
    ttk.Button(root, text ='Next',command = root.destroy).place(x=420,y=475)
    #B1.pack(side = tk.RIGHT)
    #this will run the mainloop.
    root.mainloop()
    return xval
            
