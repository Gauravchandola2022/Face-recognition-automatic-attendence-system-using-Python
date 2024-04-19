from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#screen dimensions
        self.root.title("Face Recognition System")


        # ************variables*********************
        self.var_dep=String=StringVar()
        self.var_course=String=StringVar()
        self.var_year=String=StringVar()
        self.var_semester=String=StringVar()
        self.va_std_id=String=StringVar()
        self.var_std_name=String=StringVar()
        self.var_section=String=StringVar()
        self.var_roll=String=StringVar()
        self.var_gender=String=StringVar()
        self.var_dob=String=StringVar()
        self.var_email=String=StringVar()
        self.var_phone=String=StringVar()
        self.var_address=String=StringVar()
        self.var_teacher=String=StringVar()
        

        img=Image.open(r"images_collage\student_1.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        img1=Image.open(r"images_collage\Face-Recognition-Automatic-Attendance-System.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open(r"images_collage\student_2.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3=Image.open(r"images_collage\pngtree-blue-face-recognition-bio-technology-poster-background-image_195699.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"images_collage\student_profile_icon.gif")
        img_left=img_left.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #CURRENT COURSE INFO
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=710,height=120)


        #department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","ARTS","COMMERCE","COMPUTER SCIENCE","CIVIL","MECHANICAL","ELECRICAL","MANAGEMENT","ELECTRONICS","MEDICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        #course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","Btech","MCA","BBA","MBA","MCA","BCA","B.PHARMA.","NURSING","B.COM.")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information INFO
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=255,width=710,height=300)

        #student id
        studentid_label=Label(class_student_frame,text="Student Id:",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #section
        section_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        section_combo=ttk.Combobox(class_student_frame,textvariable=self.var_section,font=("times new roman",13,"bold"),state="readonly",width="18")
        section_combo["values"]=("Select Section","A","B","C","D","E","F","G")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no.
        rollno_label=Label(class_student_frame,text="Roll.No.:",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        mail_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",13,"bold"),bg="white")
        mail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        mail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text="Contact No.:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teachers name
        teacher_label=Label(class_student_frame,text="CC Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=700,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=1,y=235,width=700,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset, width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample", width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame****************************************************
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        img_right=Image.open(r"images_collage\149006-004-054D0878.webp")
        img_right=img_right.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # ********search system**********

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=7,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No.","Contact No.","Student Name","Student Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search", width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4,pady=5,sticky=W)

        show_all_btn=Button(search_frame,text="Show all", width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4,pady=5,sticky=W)

        # ***********table frame***********

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=205,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep.","course","year","sem","id","name","section","roll no.","gender","dob","email","phone no.","address","cc name","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep.",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("roll no.",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no.",text="Contact No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("cc name",text="CC Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep.",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll no.",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("phone no.",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("cc name",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ******************function declaration******************************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="220113238",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.va_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_section.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()
                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)           
        
             
 # ***************fetch data********************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="220113238",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

#    ********************get cursor***********************
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),         
       self.var_course.set(data[1]),         
       self.var_year.set(data[2]),         
       self.var_semester.set(data[3]),         
       self.va_std_id.set(data[4]),         
       self.var_std_name.set(data[5]),         
       self.var_section.set(data[6]),         
       self.var_roll.set(data[7]),         
       self.var_gender.set(data[8]),         
       self.var_dob.set(data[9]),         
       self.var_email.set(data[10]),         
       self.var_phone.set(data[11]),         
       self.var_address.set(data[12]),         
       self.var_teacher.set(data[13]),         
       self.var_radio1.set(data[14])

    # update function    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to uodate this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="220113238",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                self.var_dep.get(),                                 
                                                self.var_course.get(),                                 
                                                self.var_year.get(),                                 
                                                self.var_semester.get(),                                 
                                                self.var_std_name.get(),                                 
                                                self.var_section.get(),                                 
                                                self.var_roll.get(),                                 
                                                self.var_gender.get(),                                 
                                                self.var_dob.get(),                                 
                                                self.var_email.get(),                                 
                                                self.var_phone.get(),                                 
                                                self.var_address.get(),                                 
                                                self.var_teacher.get(),                                 
                                                self.var_radio1.get(),                                 
                                                self.va_std_id.get(),                                 
                                                       ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       
                    
#delete button****************************
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the data of this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="220113238",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                   
       

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   

# ***************reset button**************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("Select Gender")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

# *********************generate data set and take photo sample**************************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="220113238",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                            self.var_dep.get(),                                 
                                            self.var_course.get(),                                 
                                            self.var_year.get(),                                 
                                            self.var_semester.get(),                                 
                                            self.var_std_name.get(),                                 
                                            self.var_section.get(),                                 
                                            self.var_roll.get(),                                 
                                            self.var_gender.get(),                                 
                                            self.var_dob.get(),                                 
                                            self.var_email.get(),                                 
                                            self.var_phone.get(),                                 
                                            self.var_address.get(),                                 
                                            self.var_teacher.get(),                                 
                                            self.var_radio1.get(),                                 
                                            self.va_std_id.get()==id+1                                 
                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ***********************load predefined data on face frontal from opencv


                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scalic factor=1.3
                    # minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")           
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

   
            




 

if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()          