from tkinter import *
from PIL import ImageTk,Image
import auth
import main
from tkinter import messagebox




def dashboard():
    windows = Tk()
    windows.geometry("900x500")
    windows.title("Student DashBoard")
    windows.config(bg='#262626')
    windows.resizable(0,0)

    def exam_duration():
        messagebox.showinfo(title="Start Exam", message="You are about to take your examination.")
        windows.after(1000)
        windows.destroy()
        main.start_quiz()


    def default_home():
        p2 = Frame(windows,width=900, height=455, bg='#262626')
        p2.place(x=0, y=45)
        l1 = Label(text="DASHBOARD", fg='white', bg='#262626', font=('Comic Sans MS', 40))
        l1.place(x=290, y=150 - 45)
        l2 = Label(text=f"Welcome {auth.logged_user}", fg='white', bg='#262626', font=('Comic Sans MS', 25))
        l2.place(x=290, y=150+90)

    def home():
        p1.destroy()
        p2 = Frame(windows, width=900, height=455, bg='#262626')
        p2.place(x=0, y=45)
        l1 = Label(text="Home", fg='white', bg='#262626', font=('Comic Sans MS', 50))
        l1.place(x=290, y=150 - 45)
        harmburger()

    def exam():
        p1.destroy()
        p2 = Frame(windows, width=900, height=455, bg='#262626')
        p2.place(x=0, y=45)
        lab1 = Label(text="Examination", fg='white', bg='#262626', font=('Comic Sans MS', 40))
        lab1.place(x=290, y=150 - 45)
        test = Button(text="Take Exam", width=10, height=2, font=("Arial", 12), bg="green", border=2,
                      command=exam_duration)
        test.place(x=420, y=150+ 40)



        harmburger()

    def harmburger():
        global p1
        p1 = Frame(windows,width=300, height=500, bg='#12c4c0')
        p1.place(x=0, y=0)

        #buttons
        def butt(x, y,text, fg, bg, cmd):

            def onclick(e):
                button1['background'] = "red"
                button1['foreground'] = '#262626'
            def unclick(e):
                button1['background'] = fg
                button1['foreground'] = '#262626'


            button1 = Button(p1,
                             text=text,
                             fg='#262626',
                             bg=fg,
                             width=42,
                             height=2,
                             border=0,
                             activebackground=bg,
                             activeforeground='#262626',
                             command=cmd
                             )
            button1.bind("<Enter>", onclick)
            button1.bind("<Leave>", unclick)

            button1.place(x=x, y=y)
        butt(0,80,'H O M E','#0f9d9a', '#12c4c0', home)
        butt(0, 154, 'E X A M S', '#0f9d9a', '#12c4c0', exam)


        def delete():
            p1.destroy()
            b2 = Button(
                windows,
                border=0,
                image=img1,
                command=harmburger,
                bg="#262626",
                activebackground="#262626"

            )
            b2.place(x=5, y=8)

        global img2
        img2 = ImageTk.PhotoImage(Image.open("images/close.png"))

        Button(
            p1,
            image=img2,
            border=0,
            bg='#12c4c0',
            activebackground='#12c4c0',
            command=delete
        ).place(x=5,y=10)


    default_home()

    img1 = ImageTk.PhotoImage(Image.open("images/open.png"))
    global b2
    b2 = Button(windows, image=img1,
                command=harmburger,
                border=0,
                bg='#262626',
                activebackground='#262626')
    b2.place(x=5, y=8)


    windows.mainloop()

