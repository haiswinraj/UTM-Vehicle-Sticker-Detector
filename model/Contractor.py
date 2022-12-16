from model.VehicleOwner import *


class Contractor(VehicleOwner):
	def __init__(self, owner_id=None, vehicle=None, location=None, role=None, contractor_id=None, c_id=None, owner_name=None, owner_type=None):

		super().__init__(owner_id, vehicle, owner_name, owner_type)

		self.c_id = c_id
		self.contractor_id = contractor_id
		self.location = location
		self.role = role
		self.owner_id = owner_id

	def get_contractor_data(self):

		my_cursor = mydb.cursor(buffered=True)

		my_cursor.execute("SELECT * FROM Contractor WHERE owner_id=" + str(self.owner_id))

		rowcount = my_cursor.rowcount

		if rowcount > 0:
			for row in my_cursor:
				self.c_id = row[0]
				self.contractor_id = row[1]
				self.role = row[2]
				self.location = row[3]

	def insert_contractor_data(self, owner_id):

		my_cursor = mydb.cursor(buffered=True)

		self.vehicle.insert_vehicle_data(owner_id)

		sql = "INSERT INTO Contractor (contractor_id, role, location, owner_id) VALUES (%s, %s, %s, %s)"
		val = (self.contractor_id, self.role, self.location, owner_id)
		my_cursor.execute(sql, val)
		mydb.commit()

	def get_location(self):
		return self.location

	def get_role(self):
		return self.role

	def get_contractor_id(self):
		return self.contractor_id

	
