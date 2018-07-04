#Q.1-Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *
d={'abc':123,'def':456,'ghi':789,'jkl':987,'mno':4546,'pqr':7895,'stuc':5312}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'this is the list no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()
#Q.2- In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *
d={'abc':123,'def':456,'ghi':789,'jkl':987,'mno':4546,'pqr':7895,'stuc':5312}
def insert():
    k=e1.get()
    v=e2.get()
    d[k]=v
    l.insert(END,k)
    print(d)
    
root=Tk()
e1=Entry(root)
e1.pack()
e2=Entry(root)
e2.pack()
b=Button(root,text="insert",command=insert)
b.pack()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'this is the list no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()

