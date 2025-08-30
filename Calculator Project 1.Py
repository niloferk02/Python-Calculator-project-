from tkinter import *

# Function to update the input field
def btnclick(number):
   global value
   value =value+str(number)
   data.set(value)
   
# Function to clear the input field   
def clear():
    global value
    value=''
    data.set("")
    
# Function to evaluate the expressio    
def dot():
    global value
    value =value +"."
    data.set(value)  
    
# Function to evaluate the expression    
def equals():
    global value
    result=str(eval(value))
    data.set(result)
               
        
# Create the main window
root = Tk()
root.title("Project Calculator")
root.geometry("410x380")
root.resizable(False,False)
value=""
data=StringVar()
display=Entry(root,bg="light blue",justify="left",textvariable=data,font=("verdana",20),bd=19)
display.grid(row=0,columnspan=35)

# Button layout to Create buttons dynamically
btn7 = Button(root,text="7",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(7))
btn7.grid(row=1,column=0)


btn8 = Button(root,text="8",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(8))
btn8.grid(row=1,column=1)


btn9 = Button(root,text="9",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(9))
btn9.grid(row=1,column=2)


btn_add = Button(root,text="+",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick("+"))
btn_add.grid(row=1,column=3)


btn4 = Button(root,text="4",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(4))
btn4.grid(row=2,column=0)


btn5 = Button(root,text="5",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(5))
btn5.grid(row=2,column=1)


btn6 = Button(root,text="6",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(6))
btn6.grid(row=2,column=2)


btn_sub = Button(root,text="-",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick("-"))
btn_sub.grid(row=2,column=3)


btn1 = Button(root,text="1",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(1))
btn1.grid(row=3,column=0)


btn2 = Button(root,text="2",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(2))
btn2.grid(row=3,column=1)

btn3 = Button(root,text="3",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(3))
btn3.grid(row=3,column=2)


btn_mul = Button(root,text="*",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick("*"))
btn_mul.grid(row=3,column=3)

btn_Clr = Button(root,text="C",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=clear)
btn_Clr.grid(row=1,column=4)


btn0 = Button(root,text="0",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick(0))
btn0.grid(row=4,column=1)

btn_div = Button(root,text="/",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=lambda :btnclick("/"))
btn_div.grid(row=4,column=2)


btn_equals = Button(root,text="=",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=equals)
btn_equals.grid(row=4,column=3)


btn_dot = Button(root,text=".",font=("verdana",12,"bold"),bd=12,bg="green",fg="dark gray",width=4,height=2,command=dot)
btn_dot.grid(row=4,column=0)


# Run the application
root.mainloop()