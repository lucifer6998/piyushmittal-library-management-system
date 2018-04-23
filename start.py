from tkinter import *
import sqlite3
import datetime
t=Tk()
t.configure(background='grey')
t.title("Library Management System")
t.geometry('600x600')
conn=sqlite3.connect('library1.db')
def a(event=None):
    conn=sqlite3.connect('library1.db')
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")
    l11.configure(text="")
    p=e.get()
    r=(p,)
    c=conn.execute('SELECT name,id,phone,fine,book1_name,book2_name,last_date_of_return1,last_date_of_return2 from student WHERE id=?',r)
    data=c.fetchall()
    if data==[]:
        l1.configure(text="NO DATA!!")
        return
    ctr=len(data[0])
    f=data[0]
    s=""
    for i in range(ctr):
        if i==0:
            s=s+"Name :  "+str(f[i])+"\n"
        elif i==1:
            s=s+"ID :  "+str(f[i])+"\n"
        elif i==2:
            s=s+"Phone :  "+str(f[i])+"\n"
        elif i==3 :
            s=s+"Fine :  "+str(f[i])+"\n"
        elif i==4 :
            s=s+"Book 1 name :  "+str(f[i])+"\n"
        elif i==5 :
            s=s+"Book 2 name :  "+str(f[i])+"\n"
        elif i==6 :
            s=s+"Last date of submittion for book 1 :  "+str(f[i])+"\n"
        else:
            s=s+"Last date of submittion for book 2:  "+str(f[i])+"\n"
    l1.configure(text=(s))
    l13.configure(text="")
    conn.close()

def sub():
    n=e1.get()
    i=e2.get()
    p=int(e3.get())
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    conn=sqlite3.connect('library1.db')
    conn.execute('insert into student VALUES(?,?,?,NULL,NULL,NULL,NULL,NULL)',(n,i,p))
    l11.configure(text="Submitted Successfully")
    l1.configure(text="")
    conn.commit()
    conn.close()

def issue1():
    book2=e5.get()
    ii=e7.get()
    conn=sqlite3.connect('library1.db')
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    conn.execute('update student SET book1_name=? where id=?',(book2,ii))
    conn.execute('update student SET last_date_of_return1=? where id=?',(d1,ii))
    conn.commit()
    conn.close()
    l13.configure(text="BOOK ISSUED")

def issue2():
    book2=e6.get()
    ii=e7.get()
    conn=sqlite3.connect('library1.db')
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    conn.execute('update student SET book2_name=? where id=?',(book2,ii))
    conn.execute('update student SET last_date_of_return2=? where id=?',(d1,ii))
    conn.commit()
    conn.close()
    l13.configure(text="BOOK ISSUED")

def ret1():
    ii=e7.get()
    conn=sqlite3.connect('library1.db')
    conn.execute('update student SET book1_name=NULL where id=?',(ii,))
    conn.execute('update student SET last_date_of_return1=NULL where id=?',(ii,))
    conn.commit()
    conn.close()
    l13.configure(text="BOOK RETURNED")

def ret2():
    ii=e7.get()
    conn=sqlite3.connect('library1.db')
    conn.execute('update student SET book2_name=NULL where id=?',(ii,))
    conn.execute('update student SET last_date_of_return2=NULL where id=?',(ii,))
    conn.commit()
    conn.close()
    l13.configure(text="BOOK RETURNED")

menu=Menu(t)
t.config(menu=menu)
fm=Menu(menu)
menu.add_cascade(label="File",menu=fm)
fm.add_command(label="Search ID",command=a)
fm.add_command(label="Submit New Entry",command=sub)
fm.add_separator()
fm.add_command(label="Exit", command=t.destroy)
hm=Menu(menu)
menu.add_cascade(label="Help",menu=hm)
hm.add_command(label="About")

t.bind('<Return>',a)
l8=Label(t,text="ENTER ID TO SEARCH",bg="red",font="Times 15 bold")
l8.place(x=10,y=10)
l=Label(t,text="Enter ID :",bg="red")
l.place(x=10,y=42)
e=Entry(t)
e.place(x=70,y=42)
b=Button(t,text="Search",command=a,bg="light blue",activebackground="red",bd=4)
b.place(x=40,y=70)
l1=Label(t,text="",bg="red")
l1.place(x=10,y=98)
l2=Label(t,text="CREATE NEW ENTRY",bg="red",font="Times 15 bold")
l2.place(x=330,y=10)
l3=Label(t,text="NAME :",bg="red")
l3.place(x=330,y=38)
e1=Entry(t)
e1.place(x=410,y=38)
l4=Label(t,text="ID :",bg="red")
l4.place(x=330,y=66)
e2=Entry(t)
e2.place(x=410,y=66)
l5=Label(t,text="Phone no:",bg="red")
l5.place(x=330,y=94)
e3=Entry(t)
e3.place(x=410,y=94)
l7=Label(t,text="Book1 Name :",bg="red")
l7.place(x=10,y=298)
e5=Entry(t)
e5.place(x=90,y=298)
l12=Label(t,text="Book2 Name :",bg="red")
l12.place(x=10,y=326)
e6=Entry(t)
e6.place(x=90,y=326)
b1=Button(t,text="Submit",command=sub,bg="light blue",activebackground="red",bd=4)
b1.place(x=330,y=150)
l11=Label(t,text="",bg="red")
l11.place(x=380,y=178)
l9=Label(t,text="ENTER ID TO ISSUE OR SUBMIT BOOKS",bg="red",font="Times 15 bold")
l9.place(x=10,y=232)
l12=Label(t,text="Enter ID :",bg="red")
l12.place(x=10,y=270)
e7=Entry(t)
e7.place(x=70,y=270)
b2=Button(t,text="Issue",command=issue1,bg="light blue",activebackground="red",bd=4)
b2.place(x=230,y=298)
b3=Button(t,text="Issue",command=issue2,bg="light blue",activebackground="red",bd=4)
b3.place(x=230,y=326)
b4=Button(t,text="Return Book 1",command=ret1,bg="light blue",activebackground="red",bd=4)
b4.place(x=100,y=360)
b5=Button(t,text="Return Book 2",command=ret2,bg="light blue",activebackground="red",bd=4)
b5.place(x=200,y=360)
l13=Label(t,text="",bg="red")
l13.place(x=50,y=388)
l14=Label(t,text="CREATED BY : PIYUSH MITTAL",bg="black",fg="red",font="Times 16 bold")
l14.place(x=90,y=450)
t.mainloop()
