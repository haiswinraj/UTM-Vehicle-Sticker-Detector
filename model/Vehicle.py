from controller.Database import mydb


class Vehicle:

	def __init__(self, vehicle_id=None, sticker=None, vehicle_name=None, vehicle_no=None):
		self.vehicle_name = vehicle_name
		self.vehicle_id = vehicle_id
		self.vehicle_no = vehicle_no
		self.sticker = sticker

	def get_vehicle_data(self):
		owner_id = 0
		mycursor = mydb.cursor(buffered=True)

		print(self.vehicle_id)

		mycursor.execute("SELECT * FROM Vehicle WHERE vehicle_id=" + str(self.vehicle_id))

		rowcount = mycursor.rowcount

		if rowcount > 0:
			for row in mycursor:
				self.vehicle_no = row[2]
				self.vehicle_name = row[3]

				owner_id = row[4]

		return owner_id

	def insert_vehicle_data(self, owner_id):
		my_cursor = mydb.cursor(buffered=True)

		sql = "INSERT INTO Vehicle (vehicle_name, vehicle_no, owner_id) VALUES (%s, %s, %s)"
		val = (self.vehicle_name, self.vehicle_no, owner_id)
		my_cursor.execute(sql, val)
		mydb.commit()

		vehicle_id = my_cursor.lastrowid

		self.sticker.insert_sticker_data(vehicle_id)

	def get_vehicle_name(self):
		return self.vehicle_name

	def get_vehicle_id(self):
		return self.vehicle_id 

	def get_vehicle_no(self):
		return self.vehicle_no

	def get_sticker_status(self):
		return self.sticker.get_status()

	def get_sticker_id(self):
		return self.sticker.get_sticker_id()

	def get_serial_key(self):
		return self.sticker.get_serial_key()
		
		
		

