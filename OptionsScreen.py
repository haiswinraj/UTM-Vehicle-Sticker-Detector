from tkinter import *
import RegisterStickerScreen as RSS


class OptionsScreen:

    def __init__(self, window, registerContoller):
        self.registerStickerController = registerContoller

        self.window = window
        window_height = 230
        window_width = 400

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.resizable(0, 0)
        self.window.state('normal')
        self.window.title('REGISTER STICKER')
        self.window.config(bg='#780808')

        self.lgn_frame = Frame(self.window, bg='#780808', width=400, height=700)
        self.lgn_frame.place(x=0, y=0)
        self.txt = "Owner Type"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 17, "bold"), bg="#780808", fg='white', bd=5, relief=FLAT)
        self.heading.place(x=200, y=40, anchor=CENTER)

        self.student = Button(self.window, text='STUDENT', font=("yu gothic ui", 13, "bold"), width=30, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=lambda:self.top("student"))
        self.student.place(x=50, y=80)

        self.staff = Button(self.window, text='STAFF', font=("yu gothic ui", 13, "bold"), width=30, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=lambda:self.top("staff"))
        self.staff.place(x=50, y=120)

        self.contractor = Button(self.window, text='CONTRACTOR', font=("yu gothic ui", 13, "bold"), width=30, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=lambda:self.top("contractor"))
        self.contractor.place(x=50, y=160)

    def top(self, owner_type):
        win = Toplevel(self.window)
        registerView = RSS.RegisterStickerScreen(win, owner_type, self.registerStickerController)
        self.registerStickerController.set_view(registerView)
        win.grab_set()