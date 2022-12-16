from model.History import History
from model.Vehicle import *
from model.Student import *
from model.Staff import *
from model.Contractor import *
from model.Sticker import *


class HistoryController:
    def __init__(self):
        self.view = None

    def set_view(self, view):
        self.view = view

    def save_history(self, owner):
        history = History(None, owner.get_sticker_id(), owner.get_vehicle_name(), owner.get_vehicle_no(), owner.get_serial_key(), owner.get_sticker_status(), owner.get_owner_type())
        history.insert_history_data()

    def get_history_detail(self, serial_no):

        sticker = Sticker(serial_no)
        vehicle_id = sticker.get_sticker_data()
        vehicle = Vehicle(vehicle_id, sticker)
        owner_id = vehicle.get_vehicle_data()
        sticker_color = sticker.get_sticker_color()

        if sticker_color == "red":

            student = Student(owner_id, vehicle)
            student.get_student_data()
            student.get_data()

            self.view.display_sticker(student, 'student')

        elif sticker_color == "blue":

            staff = Staff(owner_id, vehicle)
            staff.get_staff_data()
            staff.get_data()

            self.view.display_sticker(staff, 'staff')

        else:

            contractor = Contractor(owner_id, vehicle)
            contractor.get_contractor_data()
            contractor.get_data()

            self.view.display_sticker(contractor, 'contractor')

