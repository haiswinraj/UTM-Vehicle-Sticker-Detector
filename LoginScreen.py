from tkinter import *
from PIL import ImageTk, Image
import HomeScreen as home
import SignUpScreen as signUp
from controller.AuthenticateController import AuthenticateController as auth
from controller.ImageProcessingController import ImageProcessingController

class LoginScreen:
    def __init__(self, window):
        self.window = window

        window_height = 700
        window_width = 400

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.resizable(0, 0)
        self.window.state('normal')
        self.window.title('UTM VEHICLE STICKER DETECTION SYSTEM')

        # LOGIN LABEL
        # ===============================================================================================================================================================

        self.lgn_frame = Frame(self.window, bg='#780808', width=400, height=700)
        self.lgn_frame.place(x=0, y=0)
        self.txt = "LOGIN"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#780808", fg='white', bd=5, relief=FLAT)
        self.heading.place(x=50, y=100, width=300, height=30)

        # USERNAME
        # ==================================================================================================================================================================

        self.name_var = StringVar()
        self.passw_var = StringVar()

        self.username_label = Label(self.lgn_frame, text="Username", bg="#780808", fg="white",
                                   font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=50, y=300)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui ", 12, "bold"), textvariable=self.name_var)
        self.username_entry.place(x=80, y=333, width=270)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.username_line.place(x=50, y=359)

        # icon in entry --------------------------------------------------------------   
        self.username_icon = Image.open('assets/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#780808')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=50, y=332)

        # PASSWORD
        # =================================================================================================================================================================

        self.password_label = Label(self.lgn_frame, text="Password", bg="#780808", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=50, y=380)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white",font=("yu gothic ui", 12, "bold"), show="*", textvariable=self.passw_var)
        self.password_entry.place(x=80, y=412, width=244)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.password_line.place(x=50, y=440)

        # Password icon --------------------------------------------------------------
        self.password_icon = Image.open('assets/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#780808')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=50, y=414)

        # show/hide password -------------------------------------------------------------------------------
        self.show_image = ImageTk.PhotoImage(file='assets/show.png')
        self.hide_image = ImageTk.PhotoImage(file='assets/hide.png')
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=330, y=414)

        # LOGIN BUTTON
        # ==============================================================================================================================================================

        self.login = Button(self.window, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=30, bd=0, bg='#ffa90a',
                            cursor='hand2', activebackground='#ffa90a', fg='white', command=self.submit)
        self.login.place(x=200, y=480, anchor=CENTER)
        self.u_label = Label(self.window, text=" ", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.u_label.place(x=200, y=530, anchor=CENTER)
        self.no_account = Label(self.window, text="New User ?", bg="#780808", fg="white",
                                font=("yu gothic ui", 12, "bold"))
        self.no_account.place(x=115, y=553)
        self.signup = Button(self.window, text='SIGN UP', font=("yu gothic ui", 12, "bold"), width=7, bg='#780808', cursor='hand2', activebackground='#780808', fg='#ffa90a', command=self.signUp, highlightthickness=0, bd=0)
        self.signup.place(x=210, y=550)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=330, y=414)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=330, y=414)
        self.password_entry.config(show='*')

    def submit(self):
        name = self.name_var.get()
        password = self.passw_var.get()

        self.name_var.set("")
        self.passw_var.set("")

        if name != "" and password != "":
            auth_object = auth()
            rowcount = auth_object.login(name, password)

            if rowcount == 1:
                self.u_label.config(text="Loading ... ")
                self.top()
            else:
                self.u_label.config(text="Try again")
        else:
            self.u_label.config(text="Please fill up all required fields")

    def top(self):
        win = Toplevel(self.window)
        image_controller = ImageProcessingController()
        home_screen = home.HomeScreen(win, image_controller)
        image_controller.set_view(home_screen)

        self.window.withdraw()
        win.deiconify()

    def signUp(self):
        win = Toplevel(self.window)
        signUp.SignUpScreen(win)
        self.window.withdraw()
        win.deiconify()
