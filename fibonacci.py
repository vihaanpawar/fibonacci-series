from tkinter import *
root=Tk()

root.title("while loop")
root.geometry("500x500")

lbl1=Label(root,text="fibonacci series")
lbl1.pack()

lbl3=Label(root,text="enter number of terms")
lbl3.pack()

terms=Entry(root)
terms.pack()

lbl2=Label(root)
lbl2.pack()

def fibo():
    num=int (terms.get())
    firstno=0
    secondno=1
    sum=0
    counter=1
    
    while(counter<=num):
        lbl2["text"]+=str(sum)+"  "
        counter=counter+1
        firstno=secondno
        secondno=sum
        sum=firstno+secondno
        
btn=Button(root,text="show fibonicci series",command=fibo) 
btn.pack()      
root.mainloop()
