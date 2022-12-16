from datetime import datetime
from model.Contractor import *


class History:
    def __init__(self, history_id=None, sticker_id=None, vehicle_name=None, vehicle_no=None, serial_no=None, status=None, owner_type=None):
        self.history_id = history_id
        self.sticker_id = sticker_id
        self.vehicle_name = vehicle_name
        self.vehicle_no = vehicle_no
        self.serial_no = serial_no
        self.status = status
        self.owner_type = owner_type

    def insert_history_data(self):
        mycursor = mydb.cursor(buffered=True)

        sql = "INSERT INTO History (sticker_id, vehicle_name, vehicle_no, serial_no, owner_type, date, time, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.sticker_id, self.vehicle_name, self.vehicle_no, self.serial_no,
               self.owner_type, datetime.date(datetime.now()), datetime.time(datetime.now()),
               self.status)

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

