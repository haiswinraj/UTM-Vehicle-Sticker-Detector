from controller.Database import mydb


class VehicleOwner:

	def __init__(self, owner_id=None, vehicle=None, owner_name=None, owner_type=None):
		self.owner_name = owner_name
		self.owner_id = owner_id
		self.owner_type = owner_type
		self.vehicle = vehicle

	def insert_data(self):
		my_cursor = mydb.cursor(buffered=True)

		sql = "INSERT INTO VehicleOwner (owner_name, owner_type) VALUES (%s, %s)"
		val = (self.owner_name, self.owner_type)
		my_cursor.execute(sql, val)
		mydb.commit()

		return my_cursor.lastrowid

	def get_data(self):
		my_cursor = mydb.cursor(buffered=True)

		my_cursor.execute("SELECT * FROM VehicleOwner WHERE owner_id=" + str(self.owner_id))

		row_count = my_cursor.rowcount

		if row_count > 0:
			for row in my_cursor:
				self.owner_name = row[1]
				self.owner_type = row[2]

	def get_owner_name(self):
		return self.owner_name

	def get_owner_id(self):
		return self.owner_id

	def get_owner_type(self):
		return self.owner_type

	def get_vehicle_no(self):
		return self.vehicle.get_vehicle_no()

	def get_vehicle_name(self):
		return self.vehicle.get_vehicle_name()

	def get_sticker_status(self):
		return self.vehicle.get_sticker_status()

	def get_sticker_id(self):
		return self.vehicle.get_sticker_id()

	def get_serial_key(self):
		return self.vehicle.get_serial_key()
