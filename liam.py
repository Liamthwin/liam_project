from tkinter import*
window = Tk()
window.geometry("500x200")
def textbox2():
    textbox2=Message(text=data1.get())
    textbox2.place(x=155,y=70,width=200,height=25)
    textbox2["bg"]="white"
    textbox2["fg"]="black"

def textbox3():
    textbox3=Message(text=data2.get())
    textbox3.place(x=155,y=100,width=200,height=25)
    textbox3["bg"]="white"
    textbox3["fg"]="black"

data1=StringVar()
label1=Label(text="Enter Your Name: ")
label1.place(x=30,y=20)
textbox1=Entry(textvariable=data1)
textbox1.place(x=150,y=20,width=200,height=25)
textbox1["justify"]="center"

data2=StringVar()
label2=Label(text="Enter Your Age: ")
label2.place(x=30,y=40)
textbox5=Entry(textvariable=data2)
textbox5.place(x=150,y=40,width=200,height=25)
textbox5["justify"]="center"


textbox1.focus()
button=Button(text="Press Me",command=textbox2)
button.place(x=30,y=80,width=120,height=25)

textbox5.focus()
button=Button(text="Press Me",command=textbox3)
button.place(x=30,y=100,width=120,height=25)

window.mainloop()


    




