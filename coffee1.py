"""
Author: Aoua Sow
Final Project: Sow's Cofee
Date: 07/22/2024
Desc: a programm that create a coffee shop system using GUI app python tkinter.

"""




from os import W_OK 
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


 
#window
window =tk.Tk()
window.title("Sow's Coffee")  #window name
window.geometry("1200x1200")  #window size
window.config(bg="brown")     #window background

#frames

left_frame = tk.Frame(window, bg = "yellow")  #left frame
left_frame.pack(side= tk.LEFT, expand=TRUE, fill=tk.BOTH)


right_frame = tk.Frame(window,bg="yellow")   #right frame
right_frame.pack(side = tk.RIGHT, expand=FALSE)

#Function clicks
def clicked():
     value = "Thank You for your Order" + myEntry.get()
     messagebox.showinfo("order",  value)
     label.configure(text=value,)


#widgets
label1 = Label(left_frame, text="Welcome to Sow's Coffee Shop", font=80, bg="yellow")
label1.pack()

label = Label(left_frame, text= "Menu", bg="yellow", font=20,)
label.pack()

labelName = Label(left_frame, text= "Name", bg="yellow", font=20)
labelName.pack()
myEntry = Entry(left_frame, width=20,)
myEntry.pack()
foodLabel =Label(left_frame, text= "Select your Order", bg="yellow", font=20,)
foodLabel.pack()
 
#function ckeckstates with different coffee flavor
checkSate = BooleanVar()
checkSate.set(True)
myCheck1 = Checkbutton(left_frame, text="French Vanilla", bg="yellow", font=15, var=checkSate)
myCheck1.pack()
myCheck2 = Checkbutton(left_frame, text="Cappuccino", bg="yellow", font=15)
myCheck2.pack()
myCheck3 = Checkbutton(left_frame, text="House Blend", bg="yellow", font=15)
myCheck3.pack()
myCheck4 = Checkbutton(left_frame, text="Iced Coffee", bg="yellow", font=15)
myCheck4.pack()

#select mode of payement
modePaymentLabel = Label(left_frame, text="Select your Mode of Payment", bg="yellow", font=15,)
modePaymentLabel.pack()

#buttons of different mode of payement
radioState = StringVar()
radioState.set("COD")
myRadio1 = Radiobutton(left_frame, text="Debit Card", bg="yellow",  font=15, value="DC", variable= radioState)
myRadio1.pack()
myRadio2 = Radiobutton(left_frame, text="Credit Card", bg="yellow", font=15, value="CD", variable=radioState)
myRadio2.pack()
myRadio3 = Radiobutton(left_frame, text="Cash on Delivery", bg="yellow", font=15, value="COD", variable=radioState)
myRadio3.pack()
modePaymentLabel = Label(left_frame, text="Select your Mode of Payment", font=15,)

#order button
myButton = Button(left_frame, text= "Order Now", font=40, bg="brown", command=clicked)
myButton.pack()

#new window
def new():
    new = Tk()
    new.title("Sow's Coffee")
    new.configure(background="brown")
    new.geometry("500x500")

    button1 = Label(new, text="Your Order Has Been Canceled, Thank You!", font=80, bg="brown", justify="center")
    button1.pack()

     
#new window cancel order
button = Button(left_frame, text="Cancel Order", font=40, bg="brown", command=new)
button.pack(side=LEFT)

#function exit window
def new():
    window.destroy()
    new = Tk()
    new.title("Sow's Coffee")
    new.configure(background="brown")
    new.geometry("500x500")

    button3 = Label(new, text="Bye, Bye!", font=80, bg="brown", justify="center")
    button3.pack()

     
    
button2 = Button(left_frame, text="Exit", font=40, bg="brown", command= new )
button2.pack(side=RIGHT, pady=20)

 


#images
my_image = PhotoImage(file="C:/Users/aouas/OneDrive/Desktop/coffee.png")
lbn = Label(right_frame, image=my_image).pack()



#run
window.mainloop()
