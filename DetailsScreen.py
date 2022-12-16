from tkinter import *
from tkinter.font import Font


class DetailsScreen:
    def __init__(self, window, values, history_controller):
        self.history_controller = history_controller
        self.history_controller.set_view(self)
        self.window = window

        window_height = 400
        window_width = 400

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.resizable(0, 0)
        self.window.state('normal')
        self.window.title('UTM VEHICLE STICKER DETECTION SYSTEM')
        self.values = values

        self.frame = Frame(self.window, bg='white', width=400, height=700)
        self.frame.place(x=0, y=0)

        self.serial_key = self.values[0]
        self.history_controller.get_history_detail(self.serial_key)

    def display_sticker(self, owner, owner_type):

        if owner.get_sticker_status().lower() == "valid":
            status_color = "#35b537"

        else:
            status_color = "#c41d1d"

        name_font = Font(
            family='Source Sans Pro',
            size=17,
            weight='bold',
        )

        details_font = Font(
            family='yu gothic ui',
            size=15,
        )

        print(owner_type)

        if owner_type == 'student':

            owner_type_label = Label(self.frame, text = owner_type.upper(), font = name_font, fg="#c92a2a", bg="white", anchor='w')
            owner_type_label.place(x = 50, y = 30)

            student_name = Label(self.frame, text=owner.get_owner_name().upper(), font = name_font, fg="black", bg="white", anchor='w')
            student_name.place(x=50, y=60)
            student_matricid = Label(self.frame, text="Matric ID:  " + owner.get_matric_id(), font = details_font, fg="black", bg="white", anchor='w')
            student_matricid.place(x= 50, y = 110)
            student_college = Label(self.frame, text = "College:  " + owner.get_college(), font = details_font, fg="black", bg="white",anchor='w')
            student_college.place(x= 50, y = 140)
            car_plate_no = Label(self.frame, text = "Year:  " + str(owner.get_year()), font = details_font, fg="black", bg="white", anchor='w')
            car_plate_no.place(x= 50, y = 170)

        elif owner_type == 'staff':

            owner_type_label = Label(self.frame, text= owner_type.upper(), font = name_font, fg="#2a57c9", bg="white", anchor='w')
            owner_type_label.place(x= 50, y = 30)

            staff_name = Label(self.frame, text= owner.get_owner_name().upper(), font = name_font, fg="black", bg="white", anchor='w')
            staff_name.place(x= 50, y = 60)
            staff_id = Label(self.frame, text="Staff ID:  " + str(owner.get_staff_id()), font = details_font, fg="black", bg="white", anchor='w')
            staff_id.place(x= 50, y = 110)
            staff_role = Label(self.frame, text="Ocupation:  " + owner.get_role(), font = details_font, fg="black", bg="white", anchor='w')
            staff_role.place(x= 50, y = 140)
            staff_location = Label(self.frame, text="Location:  " + owner.get_location(), font = details_font, fg="black", bg="white",anchor='w')
            staff_location.place(x= 50, y = 170)

        elif owner_type == 'contractor':

            owner_type_label = Label(self.frame, text= owner_type.upper(), font = name_font, fg="#e66115", bg="white", anchor='w')
            owner_type_label.place(x= 50, y = 30)

            contractor_name = Label(self.frame, text=owner.get_owner_name().upper(), font=name_font, fg="black", bg="white",
                               anchor='w')
            contractor_name.place(x=50, y=60)
            contractor_id = Label(self.frame, text="Contractor ID:  " + str(owner.get_contractor_id()), font=details_font, fg="black",
                             bg="white", anchor='w')
            contractor_id.place(x=50, y=110)
            contractor_role = Label(self.frame, text="Ocupation:  " + owner.get_role(), font=details_font, fg="black",
                               bg="white", anchor='w')
            contractor_role.place(x=50, y=140)
            contractor_location = Label(self.frame, text="Location:  " + owner.get_location(), font=details_font, fg="black",
                                   bg="white", anchor='w')
            contractor_location.place(x=50, y=170)

        car_name = Label(self.frame, text="Car:  " + owner.get_vehicle_name(), font=details_font, fg="black", bg="white", anchor='w')
        car_name.place(x=50, y=200)
        car_plate_no = Label(self.frame, text="No:  " + owner.get_vehicle_no(), font=details_font, fg="black", bg="white", anchor='w')
        car_plate_no.place(x=50, y=230)

        sticker_status = Label(self.frame, text= "Serial Key:  " + self.serial_key, font=details_font, fg="black", bg="white", anchor='w')
        sticker_status.place(x=50, y=290)

        sticker_status_label = Label(self.frame, text="Status:  ", font = details_font, fg="black", bg="white", anchor='w')
        sticker_status_label.place(x=50, y=320)

        sticker_status = Label(self.frame, text= owner.get_sticker_status().upper(), font=details_font, fg=status_color, bg="white", anchor='w')
        sticker_status.place(x=114, y=320)