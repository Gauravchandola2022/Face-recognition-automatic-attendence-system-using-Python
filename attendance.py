from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#screen dimensions
        self.root.title("Face Recognition System")

        # ***************variables*********************
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img=Image.open(r"images_collage\stdasms.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        img1=Image.open(r"images_collage\inner-banner2.webp")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #background image
        img3=Image.open(r"images_collage\pngtree-blue-face-recognition-bio-technology-poster-background-image_195699.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",fg="red",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=510)

        img_left=Image.open(r"images_collage\student_profile_icon.gif")
        img_left=img_left.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=350)

        # labels  entry
        #attendance id
        attendanceid_label=Label(left_inside_frame,text="Student Id:",font=("times new roman",13,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #roll
        roll_label=Label(left_inside_frame,text="Roll No.:",font=("comicsansns 11 bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        roll_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=3,pady=8)
        #name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=4,pady=8)

        name_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,pady=8)
        #Department
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        department_label.grid(row=1,column=2)

        department_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        department_entry.grid(row=1,column=3,pady=8)
        #time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        # date
        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2)

        Date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,pady=8)

        #status
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly",width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons

        # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=700,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Update",command=self.update_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",fg="red",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=510)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=715,height=480)

        # ************scroll bar table***************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student Id")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=150)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# *****************fetch data************************
    def fetchData(self,rows):        
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

            # **************import csv***************
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)        
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)  

            # ***************export csv********************
    def exportCsv(self):  
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export!!!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)   
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been Exported to "+os.path.basename(fln)+" successfully")    
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   

    def get_cursor(self,event=""):            
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def update_data(self):
        try:
            # Get the selected row values
            update_id = self.var_atten_id.get()
            update_roll = self.var_atten_roll.get()
            update_name = self.var_atten_name.get()
            update_dep = self.var_atten_dep.get()
            update_time = self.var_atten_time.get()
            update_date = self.var_atten_date.get()
            update_attendance = self.var_atten_attendance.get()

            # Check if all fields are filled
            if not all([update_id, update_roll, update_name, update_dep, update_time, update_date, update_attendance]):
                messagebox.showerror("Error", "All fields are required for updating!", parent=self.root)
                return

            # Get the current data from the CSV file
            current_data = mydata

            # Find the row to update
            for i in range(len(current_data)):
                if current_data[i][0] == update_id:
                    # Update values in the row
                    current_data[i][1] = update_roll
                    current_data[i][2] = update_name
                    current_data[i][3] = update_dep
                    current_data[i][4] = update_time
                    current_data[i][5] = update_date
                    current_data[i][6] = update_attendance

                    break
            else:
                messagebox.showerror("Error", f"Student ID {update_id} not found in the CSV file!", parent=self.root)
                return

            # Update the data in the Treeview
            self.fetchData(current_data)

            # Save the updated data to the same CSV file
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Save Updated CSV",
                                             filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in current_data:
                    exp_write.writerow(i)

            messagebox.showinfo("Data Update", f"Student ID {update_id} updated and saved successfully!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def reset_data(self):    
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")


       








if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 