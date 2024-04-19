from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # screen dimensions
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="orange", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images_collage\programming-code-abstract-technology-background-of-software-developer-picture-id1304628950.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # ******************frame******************

        main_frame = Frame(f_lbl, bd=2, bg="light blue")
        main_frame.place(x=0, y=0, width=600, height=600)

        img_top1 = Image.open(r"images_collage\IMG_20230916_184306_829.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=395, y=0, width=200, height=200)

        # Developer info
        dev_label = Label(main_frame, text="Hi there, I'm Gaurav Chandola", font=("times new roman", 22, "bold"), bg="light blue")
        dev_label.place(x=2, y=5)

        dev1_label = Label(main_frame, text="A Full Stack Python Developer, ", font=("times new roman", 20, "bold"), bg="light blue")
        dev1_label.place(x=0, y=45)

        dev2_label = Label(main_frame, text="and a Frontend Web Developer, ", font=("times new roman", 20, "bold"), bg="light blue")
        dev2_label.place(x=0, y=85)

        # Buttons for GitHub and LinkedIn
        github_button = Button(main_frame, text="GitHub", command=self.visit_github, font=("times new roman", 16, "bold"), bg="green", fg="white")
        github_button.place(x=150, y=150)

        linkedin_button = Button(main_frame, text="LinkedIn", command=self.visit_linkedin, font=("times new roman", 16, "bold"), bg="green", fg="white")
        linkedin_button.place(x=250, y=150)

    def visit_github(self):
        webbrowser.open("https://github.com/Gauravchandola2022")  # Replace with the actual GitHub profile link

    def visit_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/gaurav-chandola-228498283/")  # Replace with the actual LinkedIn profile link


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()