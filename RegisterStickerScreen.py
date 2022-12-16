from tkinter import *
from tkcalendar import DateEntry


class RegisterStickerScreen:
    def __init__(self, window, owner_type, register_controller):
        self.register_controller = register_controller
        self.register_controller.set_view(self)
        self.window = window
        window_height = 700
        window_width = 400

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.resizable(0, 0)
        self.window.state('normal')

        # variables
        self.owner = owner_type
        self.name = StringVar()
        self.matric_id = StringVar()
        self.college = StringVar()
        self.year = StringVar()
        self.vehicle_no = StringVar()
        self.vehicle_name = StringVar()
        self.serial_key = StringVar()
        self.expiration_date = StringVar()
        self.status = StringVar()
        self.location = StringVar()
        self.staff_id = StringVar()
        self.contractor_id = StringVar()
        self.role = StringVar()

        self.window.title("REGISTER " + owner_type.upper() + " STICKER")

        self.collegeOptions = [
            "KTDI",
            "KTHO",
            "KTC",
            "KDOJ",
            "KTF",
            "KRP",
            "K10",
            "K09"
        ]

        self.college.set("Choose college")

        self.yearOptions = [
            "1",
            "2",
            "3",
            "4"
        ]

        self.year.set("Choose year of study")

        self.staffRoleOptions = [
            "Lecturer",
            "Staff",
        ]

        self.role.set("Choose year occupation")

        self.conRoleOptions = [
            "Cafe owner",
            "Cook"
        ]

        self.staffLocationOptions = [
            "FABU",
            "FC",
            "FE",
            "FS"
        ]

        self.conLocationOptions = [
            "Cafe Cengal",
            "Cafe Meranti",
            "Mangga",
        ]

        self.location.set("Choose working venue")

        self.lgn_frame = Frame(self.window, bg='#780808', width=400, height=700)
        self.lgn_frame.place(x=0, y=0)

        # NAME ==================================================================================================================================================================

        self.name_label = Label(self.lgn_frame, text="Name", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.name_label.place(x=50, y=30)
        self.name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui ", 12, "bold"), textvariable=self.name)
        self.name_entry.place(x=50, y=60, width=270)
        self.name_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.name_line.place(x=50, y=80)

        if self.owner.lower() == "student":

            # MATRIC ID =================================================================================================================================================================

            self.matricid_label = Label(self.lgn_frame, text="Matric ID", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
            self.matricid_label.place(x=50, y=90)
            self.matricid_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable=self.matric_id)
            self.matricid_entry.place(x=50, y=120, width=244)
            self.matricid_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
            self.matricid_line.place(x=50, y=140)

            # COLLEGE =================================================================================================================================================================


            self.college_label = Label(self.lgn_frame, text="College", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
            self.college_label.place(x=50, y=395)
            self.college_entry = OptionMenu(self.lgn_frame, self.college, *self.collegeOptions)
            self.college_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.college_entry.place(x=50, y=425, width=300)
            self.college_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")

            # YEAR =================================================================================================================================================================

            self.year_label = Label(self.lgn_frame, text="Year of Study", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
            self.year_label.place(x=50, y=465)
            self.year_entry= OptionMenu(self.lgn_frame, self.year, *self.yearOptions)
            self.year_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.year_entry.place(x=50, y=495, width=300)
            self.year_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")


        elif self.owner.lower() == "staff":

            # STAFF ID =================================================================================================================================================================

            self.staffid_label = Label(self.lgn_frame, text="Staff ID", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
            self.staffid_label.place(x=50, y=90)
            self.staffid_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable= self.staff_id)
            self.staffid_entry.place(x=50, y=120, width=244)
            self.staffid_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
            self.staffid_line.place(x=50, y=140)

            # LOCATION =================================================================================================================================================================

            self.location_label = Label(self.lgn_frame, text="Location", bg="#780808", fg="white",
                                        font=("yu gothic ui", 13, "bold"))
            self.location_label.place(x=50, y=395)
            self.location_entry = OptionMenu(self.lgn_frame, self.location, *self.staffLocationOptions)
            self.location_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.location_entry.place(x=50, y=425, width=300)
            self.location_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")

            # ROLE =================================================================================================================================================================

            self.role_label = Label(self.lgn_frame, text="Role", bg="#780808", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
            self.role_label.place(x=50, y=465)
            self.role_entry = OptionMenu(self.lgn_frame, self.role, *self.staffRoleOptions)
            self.role_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.role_entry.place(x=50, y=495, width=300)
            self.role_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")

        else:

            # CONTRACTOR ID =================================================================================================================================================================

            self.contractorid_label = Label(self.lgn_frame, text="Contractor ID", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
            self.contractorid_label.place(x=50, y=90)
            self.contractorid_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable= self.contractor_id)
            self.contractorid_entry.place(x=50, y=120, width=244)
            self.contractorid_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
            self.contractorid_line.place(x=50, y=140)

            # LOCATION =================================================================================================================================================================

            self.location_label = Label(self.lgn_frame, text="Location", bg="#780808", fg="white",
                             font=("yu gothic ui", 13, "bold"))
            self.location_label.place(x=50, y=395)
            self.location_entry = OptionMenu(self.lgn_frame, self.location, *self.conLocationOptions)
            self.location_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.location_entry.place(x=50, y=425, width=300)
            self.location_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")

            # ROLE =================================================================================================================================================================

            self.role_label = Label(self.lgn_frame, text="Role", bg="#780808", fg="white",
                         font=("yu gothic ui", 13, "bold"))
            self.role_label.place(x=50, y=465)
            self.role_entry = OptionMenu(self.lgn_frame, self.role, *self.conRoleOptions)
            self.role_entry.config(font=("yu gothic ui", 12, "bold"), bg="#780808", fg="white")
            self.role_entry.place(x=50, y=495, width=300)
            self.role_entry["menu"].config(font=("yu gothic ui", 12, "bold"), fg="#780808")

        # VEHICLE NAME =================================================================================================================================================================

        self.vehicle_name_label = Label(self.lgn_frame, text="Vehicle Name", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.vehicle_name_label.place(x=50, y=150)
        self.vehicle_name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable= self.vehicle_name)
        self.vehicle_name_entry.place(x=50, y=180, width=244)
        self.vehicle_name_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.vehicle_name_line.place(x=50, y=200)

        # VEHICLE NO =================================================================================================================================================================

        self.vehicle_no_label = Label(self.lgn_frame, text="Plate No", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.vehicle_no_label.place(x=50, y=210)
        self.vehicle_no_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable= self.vehicle_no)
        self.vehicle_no_entry.place(x=50, y=240, width=244)
        self.vehicle_no_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.vehicle_no_line.place(x=50, y=260)

        # SERIAL KEY =================================================================================================================================================================

        self.serial_key_label = Label(self.lgn_frame, text="Serial Key (Numbers only*)", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.serial_key_label.place(x=50, y=270)
        self.serial_key_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"), textvariable= self.serial_key)
        self.serial_key_entry.place(x=50, y=300, width=244)
        self.serial_key_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="white", highlightthickness=0)
        self.serial_key_line.place(x=50, y=320)

        # EXP DATE =================================================================================================================================================================

        self.expiration_date_label = Label(self.lgn_frame, text="EXP Date", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.expiration_date_label.place(x=50, y=330)
        self.expiration_date_entry = DateEntry(self.lgn_frame, selecmode='day', year=2021, month=7, day=16, highlightthickness=0, relief=FLAT, bg="#780808", fg="white", font=("yu gothic ui", 12, "bold"),
                                               textvariable=self.expiration_date, selectmode='day', date_pattern='dd-MM-yyyy')
        self.expiration_date_entry.place(x=50, y=360, width=300)

        # REGISTER STCIKER BUTTON ==============================================================================================================================================================

        self.register = Button(self.window, text='REGISTER', font=("yu gothic ui", 13, "bold"), width=30, bd=0, bg='#ffa90a', cursor='hand2', activebackground='#ffa90a', fg='white', command=self.submit)
        self.register.place(x=200, y=600, anchor=CENTER)

        self.u_label = Label(self.window, text=" ", bg="#780808", fg="white", font=("yu gothic ui", 13, "bold"))
        self.u_label.place(x=200, y=650, anchor=CENTER)

    def show_error_message(self, error_type):
        if error_type == 1:
            self.u_label.config(text="Try again")
        else:
            self.u_label.config(text="Please fill up all required fields")

    def show_success_message(self):
        self.u_label.config(text="Registered Successfully")

    def submit(self):

        stickerInfo = {}

        self.expiration_date = self.expiration_date_entry.get_date().strftime("%Y-%m-%d")

        stickerInfo['owner_type'] = self.owner
        stickerInfo['name'] = self.name.get()
        stickerInfo['matric_id'] = self.matric_id.get()
        stickerInfo['college'] = self.college.get()
        stickerInfo['year'] = self.year.get()
        stickerInfo['vehicle_no'] = self.vehicle_no.get()
        stickerInfo['vehicle_name'] = self.vehicle_name.get()
        stickerInfo['serial_key'] = self.serial_key.get()
        stickerInfo['expiration_date'] = self.expiration_date
        stickerInfo['location'] = self.location.get()
        stickerInfo['staff_id'] = self.staff_id.get()
        stickerInfo['contractor_id'] = self.contractor_id.get()
        stickerInfo['role'] = self.role.get()

        self.register_controller.register_sticker(stickerInfo)









