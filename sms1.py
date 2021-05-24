from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
import pymysql
import time
from tkinter import ttk
import pandas



def AddStudent():
    def submitadd():
        id_ = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addrvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m%Y")

        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id_, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification', 'Id() Name() Added Successfully. Clean the form')
            if (res == True):
                idvar.set('')
                namevar.set('')
                mobilevar.set('')
                emailvar.set('')
                addrvar.set('')
                gendervar.set('')
                dobvar.set('')


        except:
            messagebox.showerror('Notification','Id already exists. Try another Id',parent=addroot)

        strr ='select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        DisplayTable.delete(*DisplayTable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            DisplayTable.insert('',END, values=vv)

    # ----------------------------DEFINING GEOMETRY OF ADD STUDENT TOPLEVEL SCREEN-------------------------------
    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry('470x450+450+200')
    #addroot.iconbitmap('id.ico')
    addroot.config(bg='snow2')
    addroot.resizable(False, False)

    # --------------------------DEFINING VARIABLES USED IN ADD STUDENT FORM----------------------------------------
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addrvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()

    # -------------------------CREATING THE FORM LAYOUT-----------------------------------------------------------------
    Idlabel = Label(addroot, text=" Enter Id:", bg='midnight blue', fg='white', font=('Times New Roman', 15, 'bold'),
                    relief=RIDGE, borderwidth=3
                    , width=12, anchor='w')
    Idlabel.place(x=10, y=30)
    IdEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=idvar)
    IdEntry.place(x=200, y=30)

    namelabel = Label(addroot, text=" Enter Name:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    namelabel.place(x=10, y=80)
    nameEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=namevar)
    nameEntry.place(x=200, y=80)

    mobilelabel = Label(addroot, text=" Enter MobileNo.:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    mobilelabel.place(x=10, y=130)
    mobileEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=mobilevar)
    mobileEntry.place(x=200, y=130)

    emaillabel = Label(addroot, text=" Enter Email:", bg='midnight blue', fg='white',
                       font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                       , width=12, anchor='w')
    emaillabel.place(x=10, y=180)
    emailEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                       textvariable=emailvar)
    emailEntry.place(x=200, y=180)

    addresslabel = Label(addroot, text=" Enter Address:", bg='midnight blue', fg='white',
                         font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                         , width=12, anchor='w')
    addresslabel.place(x=10, y=230)
    addressEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                         textvariable=addrvar)
    addressEntry.place(x=200, y=230)

    genderlabel = Label(addroot, text=" Enter Gender:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    genderlabel.place(x=10, y=280)
    genderEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=gendervar)
    genderEntry.place(x=200, y=280)

    doblabel = Label(addroot, text=" Enter D.O.B:", bg='midnight blue', fg='white',
                     font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                     , width=12, anchor='w')
    doblabel.place(x=10, y=330)
    dobEntry = Entry(addroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=dobvar)
    dobEntry.place(x=200, y=330)

    submitbtn = Button(addroot, text="Submit", font=('Times New Roman', 15, 'bold'), width=20, bg='snow2',
                       activebackground='midnight blue', activeforeground='white',command=submitadd)
    submitbtn.place(x=125, y=380)

    addroot.mainloop()


# =========================================================================================================================================================================================


def SearchStudent():
    def search():
        id_ = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addrvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        addeddate = time.strftime("%d/%m%Y")
        if (id_ !=''):
            strr= 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id_))
            datas = mycursor.fetchall()
            DisplayTable.delete(*DisplayTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                DisplayTable.insert('', END, values=vv)

        elif (name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            DisplayTable.delete(*DisplayTable.get_children())
            for i in datas:
                 vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                 DisplayTable.insert('', END, values=vv)

        elif  (mobile != ''):
                strr = 'select * from studentdata where mobile=%s'
                mycursor.execute(strr, (mobile))
                datas = mycursor.fetchall()
                DisplayTable.delete(*DisplayTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    DisplayTable.insert('', END, values=vv)

        elif (email != ''):
                strr = 'select * from studentdata where email=%s'
                mycursor.execute(strr, (email))
                datas = mycursor.fetchall()
                DisplayTable.delete(*DisplayTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    DisplayTable.insert('', END, values=vv)

        elif (address != ''):
                strr = 'select * from studentdata where address=%s'
                mycursor.execute(strr, (address))
                datas = mycursor.fetchall()
                DisplayTable.delete(*DisplayTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    DisplayTable.insert('', END, values=vv)

        elif (gender != ''):
                strr = 'select * from studentdata where gender=%s'
                mycursor.execute(strr, (gender))
                datas = mycursor.fetchall()
                DisplayTable.delete(*DisplayTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    DisplayTable.insert('', END, values=vv)

        elif (dob != ''):
                    strr = 'select * from studentdata where dob=%s'
                    mycursor.execute(strr, (dob))
                    datas = mycursor.fetchall()
                    DisplayTable.delete(*DisplayTable.get_children())
                    for i in datas:
                        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                        DisplayTable.insert('', END, values=vv)

        elif (addeddate != ''):
                strr = 'select * from studentdata where addeddate=%s'
                mycursor.execute(strr, (addeddate))
                datas = mycursor.fetchall()
                DisplayTable.delete(*DisplayTable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    DisplayTable.insert('', END, values=vv)



    # ----------------------------DEFINING GEOMETRY OF SEARCH STUDENT TOPLEVEL SCREEN-------------------------------
    searchroot = Toplevel()
    searchroot.grab_set()
    searchroot.geometry('470x500+450+250')
    #searchroot.iconbitmap('id.ico')
    searchroot.config(bg='snow2')
    searchroot.resizable(False, False)

    # --------------------------DEFINING VARIABLES USED IN SEARCH STUDENT FORM----------------------------------------
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addrvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()
    datevar = StringVar()

    # -------------------------CREATING THE FORM LAYOUT-----------------------------------------------------------------
    idlabel = Label(searchroot, text=" Enter Id:", bg='midnight blue', fg='white', font=('Times New Roman', 15, 'bold'),
                    relief=RIDGE, borderwidth=3
                    , width=12, anchor='w')
    idlabel.place(x=10, y=30)
    idEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=idvar)
    idEntry.place(x=200, y=30)

    namelabel = Label(searchroot, text=" Enter Name:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    namelabel.place(x=10, y=80)
    nameEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                      textvariable=namevar)
    nameEntry.place(x=200, y=80)

    mobilelabel = Label(searchroot, text=" Enter Mobile:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    mobilelabel.place(x=10, y=130)
    mobileEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=mobilevar)
    mobileEntry.place(x=200, y=130)

    emaillabel = Label(searchroot, text=" Enter Email:", bg='midnight blue', fg='white',
                       font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                       , width=12, anchor='w')
    emaillabel.place(x=10, y=180)
    emailEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                       textvariable=emailvar)
    emailEntry.place(x=200, y=180)

    addresslabel = Label(searchroot, text=" Enter Address:", bg='midnight blue', fg='white',
                         font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                         , width=12, anchor='w')
    addresslabel.place(x=10, y=230)
    addressEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                         textvariable=addrvar)
    addressEntry.place(x=200, y=230)

    genderlabel = Label(searchroot, text=" Enter Gender:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    genderlabel.place(x=10, y=280)
    genderEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=gendervar)
    genderEntry.place(x=200, y=280)

    doblabel = Label(searchroot, text=" Enter D.O.B:", bg='midnight blue', fg='white',
                     font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                     , width=12, anchor='w')
    doblabel.place(x=10, y=330)
    dobEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=dobvar)
    dobEntry.place(x=200, y=330)

    entdatelabel = Label(searchroot, text=" Enter Date:", bg='midnight blue', fg='white',
                         font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                         , width=12, anchor='w')
    entdatelabel.place(x=10, y=380)
    entdateEntry = Entry(searchroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                         textvariable=datevar)
    entdateEntry.place(x=200, y=380)

    submitbtn = Button(searchroot, text="Submit", font=('Times New Roman', 15, 'bold'), width=20, bg='snow2',
                       activebackground='midnight blue', activeforeground='white', command=search)
    submitbtn.place(x=125, y=430)

    searchroot.mainloop()


# =========================================================================================================================================================================================


def UpdateStudent():
    def update():
        id_ = idvar.get()
        name = namevar.get()
        mobile = mobilevar.get()
        email = emailvar.get()
        address = addrvar.get()
        gender = gendervar.get()
        dob = dobvar.get()
        date = datevar.get()
        time = timevar.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id_))
        con.commit()
        messagebox.showinfo('Notification','Id {} modified successfully'.format(id_))

        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        DisplayTable.delete(*DisplayTable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            DisplayTable.insert('', END, values=vv)

    # ----------------------------DEFINING GEOMETRY OF UPDATE STUDENT TOPLEVEL SCREEN-------------------------------
    updroot = Toplevel()
    updroot.grab_set()
    updroot.geometry('470x550+450+200')
    #updroot.iconbitmap('id.ico')
    updroot.config(bg='snow2')
    updroot.resizable(False, False)

    # --------------------------DEFINING VARIABLES USED IN UPDATE STUDENT FORM----------------------------------------
    idvar = StringVar()
    namevar = StringVar()
    mobilevar = StringVar()
    emailvar = StringVar()
    addrvar = StringVar()
    gendervar = StringVar()
    dobvar = StringVar()
    datevar = StringVar()
    timevar = StringVar()

    # -------------------------CREATING THE FORM LAYOUT--------------------------------------------------------------------
    idlabel = Label(updroot, text=" Enter Id:", bg='midnight blue', fg='white', font=('Times New Roman', 15, 'bold'),
                    relief=RIDGE, borderwidth=3
                    , width=12, anchor='w')
    idlabel.place(x=10, y=30)
    idEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=idvar)
    idEntry.place(x=200, y=30)

    namelabel = Label(updroot, text=" Enter Name:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    namelabel.place(x=10, y=80)
    nameEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=namevar)
    nameEntry.place(x=200, y=80)

    mobilelabel = Label(updroot, text=" Enter MobileNo.:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    mobilelabel.place(x=10, y=130)
    mobileEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=mobilevar)
    mobileEntry.place(x=200, y=130)

    emaillabel = Label(updroot, text=" Enter Email:", bg='midnight blue', fg='white',
                       font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                       , width=12, anchor='w')
    emaillabel.place(x=10, y=180)
    emailEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                       textvariable=emailvar)
    emailEntry.place(x=200, y=180)

    addrlabel = Label(updroot, text=" Enter Address:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    addrlabel.place(x=10, y=230)
    addrEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=addrvar)
    addrEntry.place(x=200, y=230)

    genderlabel = Label(updroot, text=" Enter Gender:", bg='midnight blue', fg='white',
                        font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                        , width=12, anchor='w')
    genderlabel.place(x=10, y=280)
    genderEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                        textvariable=gendervar)
    genderEntry.place(x=200, y=280)

    doblabel = Label(updroot, text=" Enter D.O.B:", bg='midnight blue', fg='white',
                     font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                     , width=12, anchor='w')
    doblabel.place(x=10, y=330)
    dobEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=dobvar)
    dobEntry.place(x=200, y=330)

    datelabel = Label(updroot, text=" Enter D.O.B:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    datelabel.place(x=10, y=330)
    dateEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=datevar)
    dateEntry.place(x=200, y=330)

    timelabel = Label(updroot, text=" Enter Time:", bg='midnight blue', fg='white',
                      font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    timelabel.place(x=10, y=380)
    timeEntry = Entry(updroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=timevar)
    timeEntry.place(x=200, y=380)

    submitbtn = Button(updroot, text="Submit", font=('Times New Roman', 15, 'bold'), width=20, bg='snow2',
                       activebackground='midnight blue', activeforeground='white', command=update)
    submitbtn.place(x=125, y=430)

    cc = DisplayTable.focus()
    content = DisplayTable.item(cc)
    is_id = content['values']
    if (len(is_id) !=0):
        idvar.set(is_id[0])
        namevar.set(is_id[1])
        mobilevar.set(is_id[2])
        emailvar.set(is_id[3])
        addrvar.set(is_id[4])
        gendervar.set(is_id[5])
        dobvar.set(is_id[6])
        datevar.set(is_id[7])
        timevar.set(is_id[8])

    updroot.mainloop()


# =========================================================================================================================================================================================


def ExitStudent():
    res = messagebox.askyesnocancel('notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()


# =========================================================================================================================================================================================

def ExportStudent():
    storepath= filedialog.askopenfilename()
    saveto = DisplayTable.get_children()
    id_,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in saveto:
        content = DisplayTable.item(i)
        storeto = content['values']
        id_.append(storeto[0]),name.append(storeto[1]),mobile.append(storeto[2]),email.append(storeto[3]),address.append(storeto[4]),gender.append(storeto[5]),dob.append(storeto[6]),addeddate.append(storeto[7]),addedtime.append(storeto[8])
        heading= ['Id','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
        df= pandas.DataFrame(list(zip(id_,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=heading)
        path = r'{}.csv'.format(storepath)
        df.to_csv(path,index=False)
        messagebox.showinfo('Notifications','Student Data is saved {}'.format(path))





# ==========================================================================================================================================================================================

def ShowStudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    DisplayTable.delete(*DisplayTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        DisplayTable.insert('', END, values=vv)


# ==========================================================================================================================================================================================


def DeleteStudent():
    cc = DisplayTable.focus()
    content = DisplayTable.item(cc)
    is_id = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(is_id))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully'.format(is_id))

    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    DisplayTable.delete(*DisplayTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        DisplayTable.insert('', END, values=vv)

# ==========================================================================================================================================================================================


def connectToDb():

    def submitdb():
        global con, mycursor
        host = hostvar.get()
        user = uservar.get()
        password = passwordvar.get()
        print(host,user,password)
        try:
            con = pymysql.connect(host= host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications',"Incorrect data. Try again")
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int, name varchar(20), mobile varchar(20), email varchar(30), address varchar (100),gender varchar(50), dob varchar(50), date varchar(50), time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created. Successfully connected to the database.', parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Successfully connected to the database.', parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+750+200')
    #dbroot.iconbitmap('id.ico')
    dbroot.config(bg='snow2')
    dbroot.resizable(False, False)

    hostvar = StringVar()
    uservar = StringVar()
    passwordvar = StringVar()

    hostlabel = Label(dbroot, text=" Enter host:", bg='midnight blue', fg='white', font=('Times New Roman', 15, 'bold'),
                      relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    hostlabel.place(x=10, y=30)
    hostEntry = Entry(dbroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=hostvar)
    hostEntry.place(x=200, y=30)

    userlabel = Label(dbroot, text=" Enter user:", bg='midnight blue', fg='white', font=('Times New Roman', 15, 'bold'),
                      relief=RIDGE, borderwidth=3
                      , width=12, anchor='w')
    userlabel.place(x=10, y=80)
    userEntry = Entry(dbroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3, textvariable=uservar)
    userEntry.place(x=200, y=80)

    passwordlabel = Label(dbroot, text=" Enter password:", bg='midnight blue', fg='white',
                          font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3
                          , width=12, anchor='w')
    passwordlabel.place(x=10, y=130)
    passwordEntry = Entry(dbroot, font=('Times New Roman', 15, 'bold'), relief=RIDGE, borderwidth=3,
                          textvariable=passwordvar)
    passwordEntry.place(x=200, y=130)

    submitbtn = Button(dbroot, text="Submit", font=('Times New Roman', 15, 'bold'), width=20, bg='snow2',
                       activebackground='midnight blue', activeforeground='white', command=submitdb)
    submitbtn.place(x=130, y=180)

    dbroot.mainloop()


# ==========================================================================================================================================================================================

root = Tk()
root.title('Student management system')
root.config(bg='red4')
root.geometry('1200x700+200+50')
#root.iconbitmap('id.ico')
root.resizable(False, False)

# ---------------------------------------DEFINING FRAMES IN ROOT--------------------------------------------------------------------------------

AddDataFrame = Frame(root, bg='midnight blue', relief=RIDGE, borderwidth=5)
AddDataFrame.place(x=15, y=100, width=500, height=550)

DisplayDataFrame = Frame(root, bg='snow2', relief=RIDGE, borderwidth=5)
DisplayDataFrame.place(x=575, y=100, width=600, height=550)

# ----------------------------------------ADDING TOP LABELS, TIME AND CONNECT TO DATABASE--------------------------------------------
disptxt = " Student Management System "
TopLabel = Label(root, text=disptxt, relief=SUNKEN, font=('Times New Roman', 30, 'bold'), borderwidth=5, bg='snow2')
TopLabel.place(x=360, y=5)

localtime = time.asctime(time.localtime(time.time()))
Clock = Label(root, text=localtime, relief=SUNKEN, font=('Times New Roman', 12, 'bold'), borderwidth=4, bg='snow2',
              width=20)
Clock.place(x=7, y=10)

ToDatabase = Button(root, text='To Database', width=20, font=('Times New Roman', 12, 'bold'), relief=SUNKEN,
                    borderwidth=4, bg='snow2',
                    activebackground='midnight blue', activeforeground='white', command=connectToDb)
ToDatabase.place(x=990, y=10)

# ------------------------------------------ADD DATA FRAME-----------------------------------------------------------------------------------

frontLabel = Label(AddDataFrame, text="SELECT OPTION", font=('Times New Roman', 24, 'bold'), bg='midnight blue',
                   fg='snow2')
frontLabel.pack(side=TOP, expand=True, pady=12)

AddBtn = Button(AddDataFrame, text="1. Add Student", relief=GROOVE, font=('Times New Roman', 15, 'bold'), borderwidth=4,
                bg='snow2', fg='red4', width=20, bd=4,
                activebackground='red4', activeforeground='white', command=AddStudent)
AddBtn.pack(side=TOP, expand=False, pady=12)

searchBtn = Button(AddDataFrame, text="2.Search Student", relief=GROOVE, font=('Times New Roman', 15, 'bold'),
                   borderwidth=4, bg='snow2', fg='red4', width=20, bd=4,
                   activebackground='red4', activeforeground='white', command=SearchStudent)
searchBtn.pack(side=TOP, expand=False, pady=12)

deleteBtn = Button(AddDataFrame, text="3.Delete Student", relief=GROOVE, font=('Times New Roman', 15, 'bold'),
                   borderwidth=4, bg='snow2', fg='red4', width=20, bd=4,
                   activebackground='red4', activeforeground='white', command=DeleteStudent)
deleteBtn.pack(side=TOP, expand=False, pady=12)

updateBtn = Button(AddDataFrame, text="4.Update Student", relief=GROOVE, font=('Times New Roman', 15, 'bold'),
                   borderwidth=4, bg='snow2', fg='red4', width=20, bd=4,
                   activebackground='red4', activeforeground='white', command=UpdateStudent)
updateBtn.pack(side=TOP, expand=False, pady=12)

showBtn = Button(AddDataFrame, text="5.Show All", relief=GROOVE, font=('Times New Roman', 15, 'bold'), borderwidth=4,
                 bg='snow2', fg='red4', width=20, bd=4,
                 activebackground='red4', activeforeground='white', command=ShowStudent)
showBtn.pack(side=TOP, expand=False, pady=12)

exportBtn = Button(AddDataFrame, text="6.Export Data", relief=GROOVE, font=('Times New Roman', 15, 'bold'),
                   borderwidth=4, bg='snow2', fg='red4', width=20, bd=4,
                   activebackground='red4', activeforeground='white', command=ExportStudent)
exportBtn.pack(side=TOP, expand=False, pady=12)

exitBtn = Button(AddDataFrame, text="7.Exit", relief=GROOVE, font=('Times New Roman', 15, 'bold'), borderwidth=4,
                 bg='snow2', fg='red4', width=20, bd=4,
                 activebackground='red4', activeforeground='white', command=ExitStudent)
exitBtn.pack(side=TOP, expand=False, pady=12)

# ------------------------------------------DISPLAY DATA FRAME--------------------------------------------------------------------------------------
style = ttk.Style()
style.configure('Treeview.Heading', font=('Times New Roman', 15, 'bold'), fg='red4')

scroll_x = Scrollbar(DisplayDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(DisplayDataFrame, orient=VERTICAL
                     )
DisplayTable = Treeview(DisplayDataFrame, columns=(
'Id', 'Name', 'MobileNo.', 'Email', 'Address', 'Gender', 'D.O.B', 'Date Mod.', 'Time Mod.'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=DisplayTable.xview)
scroll_y.config(command=DisplayTable.yview)

DisplayTable.heading('Id', text='Id')
DisplayTable.heading('Name', text='Name')
DisplayTable.heading('MobileNo.', text='MobileNo.')
DisplayTable.heading('Email', text='Email')
DisplayTable.heading('Address', text='Address')
DisplayTable.heading('Gender', text='Gender')
DisplayTable.heading('D.O.B', text='D.O.B')
DisplayTable.heading('Date Mod.', text='Date Mod.')
DisplayTable.heading('Time Mod.', text='Time Mod.')
DisplayTable['show'] = 'headings'
DisplayTable.column('Id', width=100)
DisplayTable.column('Name', width=200)
DisplayTable.column('MobileNo.', width=200)
DisplayTable.column('Email', width=300)
DisplayTable.column('Address', width=200)
DisplayTable.column('Gender', width=100)
DisplayTable.column('D.O.B', width=150)
DisplayTable.column('Date Mod.', width=150)
DisplayTable.column('Time Mod.', width=150)

DisplayTable.pack(fill=BOTH, expand=1)

# ------------------------------------------
root.mainloop()

