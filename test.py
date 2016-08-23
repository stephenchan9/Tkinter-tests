from tkinter import *

root=Tk()

#a_label=Label(root,text="this is a label")
#a_label.pack()

topFrame = Frame(root)
topFrame.pack()

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#fitting widgets into the layout.
name= Label(topFrame, text="Name:",fg="red")
name.pack(fill=X)

id= Label(topFrame, text="ID:",fg="red")
id.pack(fill=Y)

#button1= Button(topFrame,text="Button1",fg="red")
#button2= Button(topFrame,text="Button2", fg="green")

#button1.pack(side=LEFT)
#button2.pack(side=RIGHT)


#Adds entry into root
entryName=Entry(root)
entryID=Entry(root)

name.grid(row=0)
id.grid(row=1)
entryName.grid(row=0,column=1)
entryID.grid(row=1,column=1)




root.mainloop()