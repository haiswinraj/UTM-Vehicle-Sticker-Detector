import easyocr
from model.Student import *
from model.Staff import *
from model.Contractor import Contractor
from model.Sticker import Sticker
from model.Vehicle import Vehicle
from controller.HistoryController import HistoryController


class ImageProcessingController:
    def __init__(self):
        self.serial_key = None
        self.view = None
        self.History_Contoller = HistoryController()

    def set_view(self, view):
        self.view = view

    def recognize_text(self, filepath):
        # load an image and recognizes text --------------------------

        reader = easyocr.Reader(['en'], gpu=True)

        return reader.readtext(filepath)

    def validate_sticker(self, result):
        num = 0
        self.serial_key = ""

        for (bbx, text, prob) in result:

            if text == "NO SIRI:":
                num = 1
            else:
                if num == 1:
                    self.serial_key = text
                    num = 0

        print(self.serial_key, result)

        if self.serial_key.isnumeric():

            # 3. Check if database has the serial key or not

            sticker = Sticker(self.serial_key)
            vehicle_id = sticker.get_sticker_data()

            if vehicle_id is not None:
                vehicle = Vehicle(vehicle_id, sticker)
                owner_id = vehicle.get_vehicle_data()
                sticker_color = sticker.get_sticker_color()

                if sticker_color == "red":
                    student = Student(owner_id, vehicle)
                    student.get_student_data()
                    student.get_data()

                    self.view.display_sticker_info(student, 'student')
                    self.save_history(student)

                elif sticker_color == "blue":

                    staff = Staff(owner_id, vehicle)
                    staff.get_staff_data()
                    staff.get_data()

                    self.view.display_sticker_info(staff, 'staff')
                    self.save_history(staff)
                else:

                    contractor = Contractor(owner_id, vehicle)
                    contractor.get_contractor_data()
                    contractor.get_data()

                    self.view.display_sticker_info(contractor, 'contractor')
                    self.save_history(contractor)
            else:
                self.view.display_not_registered_image()
        else:
            self.view.display_no_sticker_image()

    def save_history(self, owner):
        self.History_Contoller.save_history(owner)






