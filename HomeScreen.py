from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
from tkinter.font import Font
import LoginScreen as login
import HistoryScreen as history
import OptionsScreen as options
from controller.RegisterStickerContoller import RegisterStickerController as RSC


class HomeScreen:
    def __init__(self, window, image):
        self.image_processing = image

        self.window = window
        self.window.config(bg="white")
        self.window.title("UTM VEHICLE STICKER DETECTION SYSTEM")
        window_height = 700
        window_width = 1200

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # 1-LEFT BAR ==============================================================================================================================================================================================

        self.header = Frame(self.window, width=300, height=600, bg="#780808")
        self.header.grid(rowspan=4, row=0, column=0, sticky=W+N+S)

        # UTM Logo

        self.logo = Image.open('assets/UTM-LOGO.png')
        self.newsize = (200, 200)
        self.logo = self.logo.resize(self.newsize)
        photo = ImageTk.PhotoImage(self.logo)
        self.logo_label = Label(self.window, image=photo, bg="#780808")
        self.logo_label.image = photo
        self.logo_label.place(x=45, y=55)

        # System name & buttons

        self.header_content = Frame(self.window, width=300, height=500, bg="#780808")
        self.header_content.place(x=0, y=260)
        self.system_name = Label(self.header_content, text="UTM Vehicle Sticker Detection", font=("yu gothic ui", 13, 'bold'), fg="white", bg="#780808")
        self.system_name.place(x=150, y=30, anchor=CENTER)
        self.system_name = Label(self.header_content, text="System", font=("yu gothic ui", 13, 'bold'), fg="white", bg="#780808")
        self.system_name.place(x=150, y=60, anchor=CENTER)
        self.browse_text = StringVar()
        self.browse_btn = Button(self.header_content, command=self.open_file, textvariable=self.browse_text, font=("Raleway", 12, "bold"), bg="white", fg="#ffa90a", height=2, width=16)
        self.browse_text.set("Upload Sticker")
        self.browse_btn.place(x=150, y=130, anchor=CENTER)
        self.view_history = StringVar()
        self.history_btn = Button(self.header_content, command=self.show_history, textvariable=self.view_history, font=("Raleway", 12, "bold"), bg="white", fg="#ffa90a", height=2, width=16)
        self.view_history.set("History")
        self.history_btn.place(x=150, y=190, anchor=CENTER)
        self.register_sticker = StringVar()
        self.register_btn = Button(self.header_content, command=self.show_options, textvariable=self.register_sticker, font=("Raleway", 12, "bold"), bg="white", fg="#ffa90a", height=2, width=16)
        self.register_sticker.set("New Sticker")
        self.register_btn.place(x=150, y=250, anchor=CENTER)

        self.image = Image.open('assets/logout.png')
        newsize = (30, 30)
        self.image = self.image.resize(newsize)
        photo = ImageTk.PhotoImage(self.image)

        self.logout_btn = Button(self.header_content, image=photo, command=self.logout, bg="#780808", borderwidth=0, height=30, width=30, activebackground="#780808", highlightthickness = 0, bd = 0)
        self.logout_btn.image = photo
        self.logout_btn.place(x=150, y=390, anchor=CENTER)

        # 2- CONTENT AREA ========================================================================================================================================================================================

        self.main_content = Frame(self.window, width=900, height=700, bg="white")
        self.main_content.grid(rowspan=4, row=0, columnspan=3, column=1)

        self.main_frame = Frame(self.main_content, width=900, height=700, bg="white")
        self.main_frame.grid(row=2, column=2)

        logo = Image.open('assets/4.png')
        newsize = (400, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x= 900/2, y = 700/2, anchor=CENTER)

        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(1, weight=1)

    def open_file(self):

        # Processing image ------------------------------------------------------------------
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        logo = Image.open('assets/2.png')
        newsize = (400, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x= 900/2, y = 700/2, anchor=CENTER)

        # -----------------------------------------------------------------------------------

        self.browse_text.set("Loading ... ")
        file = askopenfile(parent=self.window, mode='rb', title="Choose a file")

        self.filepath =""

        if file:
            self.filepath = os.path.abspath(file.name)

        if self.filepath!="":
            self.result = self.image_processing.recognize_text(self.filepath)
            self.image_processing.validate_sticker(self.result)

        else:

            # No File Chosen image ------------------------------------------------------------------
            for widget in self.main_frame.winfo_children():
                widget.destroy()

            logo = Image.open('assets/4.png')
            newsize = (400, 400)
            logo = logo.resize(newsize)
            logo = ImageTk.PhotoImage(logo)
            logo_label = Label(self.main_frame, image=logo, bg="white")
            logo_label.image = logo
            logo_label.place(x= 900/2, y = 700/2, anchor=CENTER)

            # -----------------------------------------------------------------------------------

        self.browse_text.set("Browse")

    def display_no_sticker_image(self):
        for widget in self.main_frame.winfo_children():
                widget.destroy()

        logo = Image.open('assets/3.png')
        newsize = (400, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x= 900/2, y = 700/2, anchor=CENTER)

        self.browse_text.set("Browse")

    def display_not_registered_image(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        logo = Image.open('assets/5.png')
        newsize = (400, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x=900 / 2, y=700 / 2, anchor=CENTER)

        self.browse_text.set("Browse")

    def display_no_file(self):
        for widget in self.main_frame.winfo_children():
                widget.destroy()

        logo = Image.open('assets/4.png')
        newsize = (400, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x=900 / 2, y=700 / 2, anchor=CENTER)

        self.browse_text.set("Browse")

    def display_sticker_info(self, owner, owner_type):
        if owner.get_sticker_status().lower() == "valid":
            status_color = "#35b537"

        else:
            status_color = "#c41d1d"

        name_font = Font(
            family = 'Source Sans Pro',
            size = 17,
            weight = 'bold',
            overstrike = False
        )

        details_font = Font(
            family = 'yu gothic ui',
            size = 15,
            overstrike = False
        )

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        logo = Image.open(self.filepath)
        newsize = (600, 400)
        logo = logo.resize(newsize)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.main_frame, image=logo, bg="white")
        logo_label.image = logo
        logo_label.place(x= 450, y = 230, anchor=CENTER)

        if owner_type == 'student':

            owner_type_label = Label(self.main_frame, text= owner_type.upper(), font = name_font, fg="#c92a2a", bg="white", anchor='w')
            owner_type_label.place(x= 150, y = 450)

            student_name = Label(self.main_frame, text= " - " + owner.get_owner_name().upper(), font = name_font, fg="black", bg="white", anchor='w')
            student_name.place(x= 273, y = 450)
            student_matricid = Label(self.main_frame, text="Matric ID: " + owner.get_matric_id(), font = details_font, fg="black", bg="white", anchor='w')
            student_matricid.place(x= 150, y = 500)
            student_college = Label(self.main_frame, text="College: " + owner.get_college(), font = details_font, fg="black", bg="white",anchor='w')
            student_college.place(x= 150, y = 530)
            car_plate_no = Label(self.main_frame, text="Year: " + str(owner.get_year()), font = details_font, fg="black", bg="white", anchor='w')
            car_plate_no.place(x= 150, y = 560)
            car_name = Label(self.main_frame, text="Car: " + owner.get_vehicle_name(), font = details_font, fg="black", bg="white", anchor='w')
            car_name.place(x= 500, y = 500)
            car_plate_no = Label(self.main_frame, text="No: " + owner.get_vehicle_no(), font = details_font, fg="black", bg="white", anchor='w')
            car_plate_no.place(x= 500, y = 530)
            sticker_status_label = Label(self.main_frame, text="Status: ", font = details_font, fg="black", bg="white", anchor='w')
            sticker_status_label.place(x= 500, y = 560)

            sticker_status = Label(self.main_frame, text= owner.get_sticker_status().upper(), font = details_font, fg=status_color, bg="white", anchor='w')
            sticker_status.place(x= 575, y = 560)

        elif owner_type == 'staff':

            owner_type_label = Label(self.main_frame, text= owner_type.upper(), font = name_font, fg="#2a57c9", bg="white", anchor='w')
            owner_type_label.place(x= 150, y = 450)

            staff_name = Label(self.main_frame, text= " - " + owner.get_owner_name().upper(), font = name_font, fg="black", bg="white", anchor='w')
            staff_name.place(x= 233, y = 450)
            staff_id = Label(self.main_frame, text="Staff ID: " + str(owner.get_staff_id()), font = details_font, fg="black", bg="white", anchor='w')
            staff_id.place(x= 150, y = 500)
            staff_role = Label(self.main_frame, text="Ocupation: " + owner.get_role(), font = details_font, fg="black", bg="white", anchor='w')
            staff_role.place(x= 150, y = 560)
            staff_location = Label(self.main_frame, text="Location: " + owner.get_location(), font = details_font, fg="black", bg="white",anchor='w')
            staff_location.place(x= 150, y = 530)
            car_name = Label(self.main_frame, text="Car: " + owner.get_vehicle_name(), font = details_font, fg="black", bg="white", anchor='w')
            car_name.place(x= 550, y = 500)
            car_plate_no = Label(self.main_frame, text="No: " + owner.get_vehicle_no(), font = details_font, fg="black", bg="white", anchor='w')
            car_plate_no.place(x= 550, y = 530)
            sticker_status_label = Label(self.main_frame, text="Status: ", font = details_font, fg="black", bg="white", anchor='w')
            sticker_status_label.place(x= 550, y = 560)

            sticker_status = Label(self.main_frame, text= owner.get_sticker_status().upper(), font = details_font, fg=status_color, bg="white", anchor='w')
            sticker_status.place(x= 625, y = 560)

        else:

            owner_type_label = Label(self.main_frame, text= owner_type.upper(), font = name_font, fg="#e66115", bg="white", anchor='w')
            owner_type_label.place(x= 150, y = 450)

            contractor_name = Label(self.main_frame, text= " - " + owner.get_owner_name().upper(), font = name_font, fg="black", bg="white", anchor='w')
            contractor_name.place(x= 290, y = 450)
            contractor_location = Label(self.main_frame, text="Location: " + owner.get_location(), font = details_font, fg="black", bg="white",anchor='w')
            contractor_location.place(x= 150, y = 500)
            contractor_role = Label(self.main_frame, text="Work: " + owner.get_role(), font = details_font, fg="black", bg="white", anchor='w')
            contractor_role.place(x= 150, y = 530)
            car_name = Label(self.main_frame, text="Car: " + owner.get_vehicle_name(), font = details_font, fg="black", bg="white", anchor='w')
            car_name.place(x= 550, y = 500)
            car_plate_no = Label(self.main_frame, text="No: " + owner.get_vehicle_no(), font = details_font, fg="black", bg="white", anchor='w')
            car_plate_no.place(x= 550, y = 530)
            sticker_status_label = Label(self.main_frame, text="Status: ", font=details_font, fg="black", bg="white", anchor='w')
            sticker_status_label.place(x= 550, y = 560)

            sticker_status = Label(self.main_frame, text= owner.get_sticker_status().upper(), font = details_font, fg=status_color, bg="white", anchor='w')
            sticker_status.place(x= 625, y = 560)

        self.browse_text.set("Browse")

    def logout(self):
        win = Toplevel(self.window)
        login.LoginScreen(win)
        self.window.withdraw()
        win.deiconify()

    def show_history(self):
        win = Toplevel(self.window)
        history.HistoryScreen(win)
        win.grab_set()

    def show_options(self):
        win = Toplevel(self.window)
        registerSticker = RSC()
        options.OptionsScreen(win, registerSticker)
        win.grab_set()










