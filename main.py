from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")


        #====All Images==========================
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = ImageTk.PhotoImage(file="images/user.jpg")
        self.pass_icon = ImageTk.PhotoImage(file="images/passLbl.PNG")
        self.label_icon = ImageTk.PhotoImage(file="images/userLbl.PNG")

        #=====Variables======
        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logo_lbl = Label(Login_Frame,image=self.user_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser = Label(Login_Frame,text="",image=self.label_icon,compound=LEFT,font=("times new roman",40,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtUser = Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblPass = Label(Login_Frame, text="", image=self.pass_icon, compound=LEFT,font=("times new roman", 40, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtPass = Entry(Login_Frame, bd=5,relief=GROOVE, textvariable=self.pass_,font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log = Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        elif self.uname.get()=="harshita" and self.pass_.get()=="123456":
            messagebox.showinfo("Successfull",f"welcome{self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid Username or Password")








root = Tk()
obj = Login_System(root)
root.mainloop()