from controller.Database import mydb
from datetime import datetime


class Sticker:
	def __init__(self, serial_key=None, expiration_date=None, status=None, sticker_color='Blue', sticker_id=None):
		self.sticker_id = sticker_id
		self.expiration_date = expiration_date
		self.status = status
		self.serial_key = serial_key
		self.sticker_color = sticker_color

	def get_sticker_data(self):
		vehicle_id = 0
		my_cursor = mydb.cursor(buffered=True)

		my_cursor.execute(
			"SELECT * FROM Sticker WHERE serial_key=" + self.serial_key)

		rowcount = my_cursor.rowcount

		if rowcount > 0:
			for row in my_cursor:
				status = self.find_sticker_status(row[2])
				vehicle_id = row[5]
				self.sticker_id = row[0]
				self.expiration_date = row[1]
				self.status = status
				self.serial_key = row[4]
				self.sticker_color = row[3]

			return vehicle_id
		else:
			return None

	def insert_sticker_data(self, vehicle_id):
		my_cursor = mydb.cursor(buffered=True)

		sql = "INSERT INTO Sticker (expiration_date, vehicle_id, serial_key, status, sticker_color) VALUES (%s, %s, %s, %s, %s)"
		val = (self.expiration_date, vehicle_id, int(self.serial_key), 'valid', 'blue')
		my_cursor.execute(sql, val)
		mydb.commit()


	def get_sticker_id(self):
		return self.sticker_id

	def get_expiration_date(self):
		return self.expiration_date

	def get_sticker_color(self):
		return self.sticker_color

	def get_status(self):
		return self.status

	def get_serial_key(self):
		return self.serial_key

	def find_sticker_status(self, date):
		current_date = datetime.date(datetime.now()).strftime("%Y-%m-%d")
		exp_date = date

		if current_date > exp_date:
			mycursor = mydb.cursor(buffered=True)
			mycursor.execute("UPDATE Sticker SET status='invalid' WHERE serial_key=" + self.serial_key)
			return "invalid"

		else:
			mycursor = mydb.cursor(buffered=True)
			mycursor.execute("UPDATE Sticker SET status='valid' WHERE serial_key=" + self.serial_key)
			return "valid"




