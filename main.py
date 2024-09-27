#import moduls
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("EMPLOYEE MANAGEMENT SYSTEM")

        # data variable
        self.vr_dep = StringVar()
        self.vr_name=StringVar()
        self.vr_desig=StringVar()
        self.vr_email=StringVar()
        self.vr_add=StringVar()
        self.vr_dob=StringVar()
        self.vr_doj=StringVar()
        self.vr_idtype=StringVar()
        self.vr_idprof=StringVar()
        self.vr_gender=StringVar()
        self.vr_marr=StringVar()
        self.vr_country=StringVar()
        self.vr_salary=StringVar()
        self.vr_phone = StringVar()

        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=('time new roman',37,'bold'),fg="red",bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        #LOGO

        img_logo=Image.open('image/emplogo.png')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        #frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=320)

        #photo
        img1 = Image.open('image/emp.jpg')
        img1 = img1.resize((1000,300))
        self.photo1= ImageTk.PhotoImage(img1)
        self.img_1 = Label(self.root, image =self.photo1)
        self.img_1.place(x=200, y=55, width=1000, height=300)

        #mainframe

        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=10, y=220, width=1500, height=560)

        #upperframe

        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white',text=("Employee Information"),font=('time new roman',11,'bold'),fg="red")
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Labels and enter fields

        #department
        lbl_dept = Label(upper_frame,text="Department",font=('arial',11,'bold'),bg="white")
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,font=('arial,12,bold'),width=17,state="readonly",textvariable=self.vr_dep)
        combo_dept["value"]=('Select Department','HR','Software Engineer','Manager')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10 ,sticky=W)

        #NAME LABEL

        lbl_Name=Label(upper_frame,font=("arial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"),textvariable=self.vr_name)
        txt_name.grid(row=1,column=1,padx=2,pady=7)

        #Designition label

        lbl_Designition=Label(upper_frame,font=("arial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"),textvariable=self.vr_desig)
        txt_Designition.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #Email

        lbl_email=Label(upper_frame,font=("areal,12,bold"),text="Email :",bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_email)
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        #address label

        lbl_address = Label(upper_frame, font=("areal,12,bold"), text="Adress :", bg="white")
        lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_add)
        txt_address.grid(row=2, column=1, padx=2, pady=7)

        #  Married status

        lbl_married_status = Label(upper_frame, font=("areal,12,bold"), text="Married Status :", bg="white")
        lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        lbl_married_com=ttk.Combobox(upper_frame,state="readonly",font=("arial",12,"bold"),width=18,textvariable=self.vr_marr)
        lbl_married_com['value']=("Married","Unmarried")
        lbl_married_com.current(0)
        lbl_married_com.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob = Label(upper_frame, font=("areal,12,bold"), text="Date of Birth :", bg="white")
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_dob)
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        #DOJ
        lbl_doj = Label(upper_frame, font=("areal,12,bold"), text="Date of Joining:", bg="white")
        lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_doj = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_doj)
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        #ID proof type
        com_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=("arial",13,"bold"),width=18,textvariable=self.vr_idtype)
        com_txt_proof['value']=("Select ID proof","PAN CARD","ADHAR CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        #id prof
        txt_proof=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"),textvariable=self.vr_idprof)
        txt_proof.grid(row=4,column=1,padx=2,pady=7)

        #Gender

        lbl_gender=Label(upper_frame,font=("arial",13,"bold"),text="Gender :" ,bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        gender_com=ttk.Combobox(upper_frame,state="readonly",font=("arial",13,"bold"),width=13,textvariable=self.vr_gender)
        gender_com['value']=("MALE","FEMALE","OTHER")
        gender_com.current(0)
        gender_com.grid(row=4,column=3,padx=2,pady=7)

        #Phone

        lbl_phone = Label(upper_frame, font=("areal,12,bold"), text="Phone:", bg="white")
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_phone = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_phone)
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

        #country

        lbl_country = Label(upper_frame, font=("areal,12,bold"), text="Country:", bg="white")
        lbl_country.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_country= ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_country)
        txt_country.grid(row=1, column=5, padx=2, pady=7)

        #salary
        lbl_salary= Label(upper_frame, font=("areal,12,bold"), text="Salary:", bg="white")
        lbl_salary.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_salary = ttk.Entry(upper_frame, width=22, font=("arial", 11, "bold"),textvariable=self.vr_salary)
        txt_salary.grid(row=2, column=5, padx=2, pady=7)

        #button frame
        button= Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button.place(x=1140, y=10, width=300, height=250)
            #ADD BUTTON
        save_button1=Button(button,text="SAVE",font=("arial",15,"bold"),width=20,bg="blue",fg="white",command=self.add_data_func)
        save_button1.grid(row=0,column=0,padx=15,pady=10)

        update_button2 = Button(button, text="UPDATE", font=("arial", 15, "bold"), width=20, bg="blue", fg="white",command=self.update_func)
        update_button2.grid(row=1, column=0, padx=15, pady=10)

        del_button3 = Button(button, text="DELETE", font=("arial", 15, "bold"), width=20, bg="blue", fg="white",command=self.del_func)
        del_button3.grid(row=2, column=0, padx=15, pady=10)

        clear_button4 = Button(button, text="CLEAR", font=("arial", 15, "bold"), width=20, bg="blue", fg="white",command=self.reset_data)
        clear_button4.grid(row=3, column=0, padx=15, pady=10)

        #down frame

        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text=("Employee Information Table"),font=('time new roman', 11, 'bold'), fg="red")
        down_frame.place(x=10, y=280, width=1480, height=270)

        #search frame

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text=("Search Employee Information"),font=('time new roman', 11, 'bold'), fg="red")
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_lbl = Label(search_frame, font=("areal,12,bold"), text="Search by:", bg="blue",fg="white")
        search_lbl.grid(row=0, column=0, sticky=W, padx=2)

        #Search by
        self.var_com_search=StringVar()
        search_com = ttk.Combobox(search_frame, state="readonly", textvariable=self.var_com_search,font=("arial", 12, "bold"), width=18)
        search_com['value'] = ("Select Option", "Phone", "id_proof")
        search_com.current(0)
        search_com.grid(row=0, column=1,sticky=W ,padx=5)

        self.var_search=StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search,width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        search_button = Button(search_frame, text="SEARCH", font=("arial", 11, "bold"), width=20,bg="blue",command=self.search_func)
        search_button.grid(row=0, column=3, padx=5)

        show_button = Button(search_frame, text="SHOW ALL",command=self.fetch_data, font=("arial", 11, "bold"), width=20,bg="blue")
        show_button.grid(row=0, column=4, padx=5)

        #----------------emp table-------------------

        #table frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        #scrollbar
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=('dep','name','desig','email','add','dob','doj','profcom','idprof','gender','marr','country','salary','phone'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_x.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text="Department")
        self.employee_table.heading('name', text="Name")
        self.employee_table.heading('desig', text="Designition")
        self.employee_table.heading('email', text="Email")
        self.employee_table.heading('add', text="Address")
        self.employee_table.heading('dob', text="DOB")
        self.employee_table.heading('doj', text="DOJ")
        self.employee_table.heading('profcom', text="ID Type")
        self.employee_table.heading('idprof', text="ID Proof")
        self.employee_table.heading('gender', text="Gender")
        self.employee_table.heading('marr', text="Married Status")
        self.employee_table.heading('country', text="Country")
        self.employee_table.heading('salary', text="Salary")
        self.employee_table.heading('phone', text="Phone")

        # fixing size
        self.employee_table['show']='headings'
        self.employee_table.column("dep",width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("desig", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("add", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("profcom", width=100)
        self.employee_table.column("idprof", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("marr", width=100)
        self.employee_table.column("country", width=100)
        self.employee_table.column("salary", width=100)
        self.employee_table.column("phone", width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.show_cursor)

        self.fetch_data()

        #save data in database function

    def add_data_func(self):
        if self.vr_dep.get() == " " or self.vr_email.get() == " ":
            messagebox.showerror("Error","Something went wrong")
        else:
            try:
                connection=mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="123456",
                    database="sys"
                 )
                my_cursor=connection.cursor()
                my_cursor.execute("insert into emp_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.vr_dep.get(),
                    self.vr_name.get(),
                    self.vr_desig.get(),
                    self.vr_email.get(),
                    self.vr_add.get(),
                    self.vr_dob.get(),
                    self.vr_doj.get(),
                    self.vr_idtype.get(),
                    self.vr_idprof.get(),
                    self.vr_gender.get(),
                    self.vr_marr.get(),
                    self.vr_country.get(),
                    self.vr_salary.get(),
                    self.vr_phone.get()

                    ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo('SUCCESS',"Employee Information has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f'due to :{str(es)}',parent=self.root)

    #fetch data into table frame

    def fetch_data(self):
        connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="123456",
            database="sys"
        )
        my_cursor = connection.cursor()
        my_cursor.execute('select * from emp_info')
        data=my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    def show_cursor(self,event):
        cursor_row=self.employee_table.focus()
        contents=self.employee_table.item(cursor_row)
        data=contents["values"]
        self.vr_dep.set(data[0]),
        self.vr_name.set(data[1]),
        self.vr_desig.set(data[2]),
        self.vr_email.set(data[3]),
        self.vr_add.set(data[4]),
        self.vr_dob.set(data[5]),
        self.vr_doj.set(data[6]),
        self.vr_idtype.set(data[7]),
        self.vr_idprof.set(data[8]),
        self.vr_gender.set(data[9]),
        self.vr_marr.set(data[10]),
        self.vr_country.set(data[11]),
        self.vr_salary.set(data[12]),
        self.vr_phone.set(data[13])

        # update table

    def update_func(self):
        if self.vr_dep.get() == " " or self.vr_email.get() == " ":
            messagebox.showerror("Error","Something went wrong")
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure you want to update?')
                if update>0:
                    connection=mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="123456",
                        database="sys"
                        )
                    my_cursor=connection.cursor()
                    my_cursor.execute('update emp_info set Department=%s,Name=%s,Designation=%s,Email=%s,addres=%s,DOB=%s,DOJ=%s,Id_proof_type=%s,Gender=%s,Married_Status=%s,Country=%s,Salary=%s,phone=%s where ID_proof =%s',(
                        self.vr_dep.get(),
                        self.vr_name.get(),
                        self.vr_desig.get(),
                        self.vr_email.get(),
                        self.vr_add.get(),
                        self.vr_dob.get(),
                        self.vr_doj.get(),
                        self.vr_idtype.get(),
                        self.vr_gender.get(),
                        self.vr_marr.get(),
                        self.vr_country.get(),
                        self.vr_salary.get(),
                        self.vr_phone.get(),
                        self.vr_idprof.get()
                    ))
                else:
                    if not update:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo(' Success' ,'Updated!',parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f'due to :{str(es)}',parent=self.root)

    #delete table
    def del_func(self):
        if self.vr_idprof.get()=="":
            messagebox.showerror("Error","ALL fields are required")
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete",parent=self.root)
                if delete>0:
                    connection = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="123456",
                        database="sys"
                    )
                    my_cursor = connection.cursor()
                    sql="delete from emp_info where ID_proof=%s "
                    value=(self.vr_idprof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo(' DELETE', 'DELETED!', parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f'due to :{str(es)}', parent=self.root)

    # clear data func
    def reset_data(self):
        self.vr_dep.set("Select Department"),
        self.vr_name.set(""),
        self.vr_desig.set(""),
        self.vr_email.set(""),
        self.vr_add.set(""),
        self.vr_dob.set(""),
        self.vr_doj.set(""),
        self.vr_idtype.set(""),
        self.vr_idprof.set("Select ID proof"),
        self.vr_gender.set("Male"),
        self.vr_marr.set("Married"),
        self.vr_country.set(""),
        self.vr_salary.set(""),
        self.vr_phone.set("")
    #search
    def search_func(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="123456",
                    database="sys"
                )
                my_cursor = connection.cursor()
                my_cursor.execute('select * from emp_info where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                    connection.commit()
                connection.close
            except Exception as es:
                messagebox.showerror("error", f'due to :{str(es)}', parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
