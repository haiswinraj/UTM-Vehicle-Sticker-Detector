from model.Sticker import Sticker
from model.Vehicle import Vehicle
from model.Student import *
from model.Staff import *
from model.Contractor import Contractor


class RegisterStickerController:
    def __init__(self):
        self.view = None
        self.owner_type = None
        self.name = None
        self.matric_id = None
        self.college = None
        self.year = None
        self.vehicle_no = None
        self.vehicle_name = None
        self.vehicle_color = None
        self.serial_key = None
        self.expiration_date = None
        self.location = None
        self.staff_id = None
        self.contractor_id = None
        self.role = None
        
    def register_sticker(self, sticker_info):

        self.owner_type = sticker_info['owner_type']
        self.name = sticker_info['name']
        self.matric_id = sticker_info['matric_id']
        self.college = sticker_info['college']
        self.year = sticker_info['year']
        self.vehicle_no = sticker_info['vehicle_no']
        self.vehicle_name = sticker_info['vehicle_name']
        self.serial_key = sticker_info['serial_key']
        self.expiration_date = sticker_info['expiration_date']
        self.location = sticker_info['location']
        self.staff_id = sticker_info['staff_id']
        self.contractor_id = sticker_info['contractor_id']
        self.role = sticker_info['role']

        empty_info = False

        if self.name != "" and self.vehicle_name != "" and self.vehicle_no != "" and self.vehicle_color != "" and self.serial_key != "" and self.expiration_date != "":

            if self.owner_type == "student":
                if self.matric_id == "" or self.college == "" or self.year == "":
                    empty_info = True

            elif self.owner_type == "staff":
                if self.location == "" or self.staff_id == "" or self.role == "":
                    empty_info = True
            else:
                if self.location == "" or self.contractor_id == "" or self.role == "":
                    empty_info = True
        else:
            empty_info = True

        if not empty_info:

            if self.serial_key.isnumeric():

                sticker = Sticker(self.serial_key, self.expiration_date, 'valid')
                vehicle = Vehicle(None, sticker, self.vehicle_name, self.vehicle_no)

                if self.owner_type == "student":
                    if self.year.isnumeric():
                        student = Student(None, vehicle, self.college, self.matric_id, self.year, None, self.name, self.owner_type)
                        owner_id = student.insert_data()
                        student.insert_student_data(owner_id)
                    else:
                        self.view.show_error_message(1)

                elif self.owner_type == "staff":
                    staff = Staff(None, vehicle, self.location, self.role, self.staff_id, None,
                                            self.name,
                                            self.owner_type)
                    owner_id = staff.insert_data()
                    staff.insert_staff_data(owner_id)

                else:
                    contractor = Contractor(None, vehicle, self.location, self.role, self.contractor_id, None, self.name, self.owner_type)
                    owner_id = contractor.insert_data()
                    contractor.insert_contractor_data(owner_id)

                self.view.show_success_message()

            else:
                self.view.show_error_message(1)
        else:
            self.view.show_error_message(2)

    def set_view(self, view):
        self.view = view