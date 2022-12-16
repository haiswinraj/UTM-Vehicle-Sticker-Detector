from model.VehicleOwner import *


class Staff(VehicleOwner):
	def __init__(self, owner_id=None, vehicle=None, location=None, role=None, staff_id=None, s_id=None, owner_name=None,
				owner_type=None):

		super().__init__(owner_id, vehicle, owner_name, owner_type)

		self.s_id = s_id
		self.staff_id = staff_id
		self.location = location
		self.role = role

	def get_staff_data(self):

		my_cursor = mydb.cursor(buffered=True)

		my_cursor.execute("SELECT * FROM Staff WHERE owner_id=" + str(self.owner_id))

		rowcount = my_cursor.rowcount

		if rowcount > 0:
			for row in my_cursor:
				self.s_id = row[0]
				self.staff_id = row[1]
				self.role = row[2]
				self.location = row[3]

	def insert_staff_data(self, owner_id):

		my_cursor = mydb.cursor(buffered=True)

		self.vehicle.insert_vehicle_data(owner_id)

		sql = "INSERT INTO Staff (staff_id, role, location, owner_id) VALUES (%s, %s, %s, %s)"
		val = (self.staff_id, self.role, self.location, owner_id)
		my_cursor.execute(sql, val)
		mydb.commit()

	def get_location(self):
		return self.location

	def get_role(self):
		return self.role

	def get_staff_id(self):
		return self.staff_id

