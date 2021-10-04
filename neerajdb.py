from tkinter import *
from tkinter import messagebox
import mysql.connector
from prettytable import from_db_cursor
root = Tk()
root.geometry('1000x680')
root.title("Form")
root.configure(background="light grey")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="neeraj"
)

def check_data():
    window=Tk()
    window.title("Show Data")
    window.geometry("1100x500")
    txtbox_8=Text(window)
    txtbox_8.place(x=5,y=5,width=1100,height=900)

    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM nnn")
    x = from_db_cursor(mycursor)
    txtbox_8.insert(INSERT,(x))

    b4=Button(window,text="Exit",bg="light grey",command=window.destroy)
    b4.place(x=430,y=410,width=170)

def entry():
    mycursor = mydb.cursor()
    firstname = txtbox_1.get()
    lastname = txtbox_2.get()
    std_id = txtbox_3.get()
    dob = txtbox_4.get()
    contact = txtbox_5.get()
    email = txtbox_6.get()
    err = bool(re.findall('\S+@\S+.\S+', email))
    address = txtbox_7.get(0.0,END)
    rollno = int(Spinbox.get(spin))
    gender = opt.get()
    if(err == True and len(contact)==10):
        nnn = "INSERT INTO nnn (First_name,Last_name,Student_ID,Gender,DOB,Contact,Email,Roll_no,Address) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)"
        val = [
            (firstname,lastname,std_id,gender,dob,contact,email,rollno,address)]
        messagebox.showinfo("Thank You","Entry Added Succesfully")
        mycursor.executemany(nnn, val)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")

    elif(len(contact)!=10):
        messagebox.showerror("ERROR","Invalid Length of Phone Number")
    elif (err != True):
        messagebox.showerror("ERROR", "Invalid Email")


label_0 = Label(root, text="STUDENT MANAGEMENT SYSTEM",bg="white",fg='black',relief='raised',font=("times new roman",18))
label_0.place(x=230,y=30,width=530)


label_1 = Label(root, text="Enter Name",relief="raised",bg="white",width=18,fg='black',font=("mongolian baiti", 16))
label_1.place(x=40,y=120)

txtbox_1 = Entry(root)
txtbox_1.place(x=310,y=120,width=250,height=27)

txtbox_2 = Entry(root)
txtbox_2.place(x=600,y=120,width=250,height=27)

label_a = Label(root, text="First Name",width=18,fg='grey',bg="light grey",font=("mongolian baiti", 15))
label_a.place(x=320,y=150)

label_b = Label(root, text="Last Name",width=18,fg='grey',bg="light grey",font=("mongolian baiti", 15))
label_b.place(x=610,y=150)


label_3 = Label(root, text="Enter Student ID",relief="raised",width=18,fg='black',bg="white",font=("mongolian baiti", 16))
label_3.place(x=40,y=240)

txtbox_3 = Entry(root)
txtbox_3.place(x=310,y=240,width=250,height=28)


label_4 = Label(root, text="Enter Date of Birth",width=18,relief="raised",fg='black',bg="white",font=("mongolian baiti", 16))
label_4.place(x=40,y=300)

txtbox_4 = Entry(root)
txtbox_4.place(x=310,y=300,width=250,height=25)

label_5 = Label(root, text="Enter Gender",width=18,relief="raised",fg='black',bg="white",font=("mongolian baiti", 16))
label_5.place(x=40,y=360)

opt = StringVar(root)
choices={"   MALE   ","   FEMALE   "}
opt.set("Select Gender")
popupMenu = OptionMenu(root,opt, *choices)
popupMenu.place(x=310,y=360,width=250)

label_6 = Label(root, text="Enter Contact Details",relief="raised",width=18,fg='black',bg="white",font=("mongolian baiti", 16))
label_6.place(x=40,y=420)

txtbox_5 = Entry(root)
txtbox_5.place(x=310,y=420,width=250,height=25)

label_7 = Label(root, text="Enter Email Address",width=18,relief="raised",fg='black',bg="white",font=("mongolian baiti", 16))
label_7.place(x=40,y=180)

txtbox_6 = Entry(root)
txtbox_6.place(x=310,y=180,width=542,height=28)

label_8 = Label(root, text="Enter Roll Number",relief="raised",width=18,fg='black',bg="white",font=("mongolian baiti", 16))
label_8.place(x=40,y=480)

spin = Spinbox(root,from_=0,to=100,width=3,font=("bold",12))
spin.place(x=310,y=480,width=250,height=28)

label_9 = Label(root, text="Enter Address",relief="raised",width=18,fg='black',bg="white",font=("mongolian baiti", 16))
label_9.place(x=40,y=540)

txtbox_7 = Text(root)
txtbox_7.place(x=310,y=540,width=542,height=75)

b1=Button(root, text='INSERT',width=7,bg="white",fg='black',command=entry)
b1.place(x=180,y=630,height=30,width=180)

b2=Button(root, text='CHECK',width=7,fg='black',bg="white",command=check_data)
b2.place(x=400,y=630,height=30,width=180)

b3=Button(root, text='EXIT',width=40,fg='black',bg="white",command=root.destroy)
b3.place(x=620,y=630,height=30,width=180)


root.mainloop()
