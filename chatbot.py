from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow



class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatterBox")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)



        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()



        img_chat=Image.open('chat.jpg')
        img_chat=img_chat.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT WITH ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        #text area scroll bar
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        #creating button
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something:",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        #entry box...
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green',)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clare.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

    # ***********************FUNCTION DECLARETION*****************************


    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


        


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END) 

        if(self.entry.get()==''):
            self.msg='Please enter some input...'
            self.label_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n'+'Bot: Hi user,how can I help you...')
        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n'+'Bot: Hello user,how can I help you...')
        elif(self.entry.get()=='hii'):
            self.text.insert(END,'\n'+'Bot: Hello user,how can I help you...')
        elif(self.entry.get()=='how are you?'):
            self.text.insert(END,'\n'+'Bot: fine and whats about you?')
        elif(self.entry.get()=='fantastic'):
            self.text.insert(END,'\n'+'Bot: Nice to hear...')
        elif(self.entry.get()=='who created you'):
            self.text.insert(END,'\n'+'Bot: Gaurav created me using python')
        elif(self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n'+'Bot: My name is chatter box.')
        elif(self.entry.get()=='can you speak in hindi'):
            self.text.insert(END,'\n'+'Bot: no, iam still learning...')
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n'+'Bot: bye, Thank you for chatting')
        elif(self.entry.get()=='who is developer?'):
            self.text.insert(END,'\n'+'Bot: developer of this project is Gaurav Chandola,and he developed this project in python language')
        else:
            self.text.insert(END,"\n\n"+"bot: Sorry, I didn't get it")    





if __name__ == '__main__':
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()     
       