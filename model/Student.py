from model.VehicleOwner import *


class Student(VehicleOwner):
	
	def __init__(self, owner_id=None, vehicle=None, college=None, matric_id=None, year=None, student_id=None, owner_name=None, owner_type=None):

		super().__init__(owner_id, vehicle, owner_name, owner_type)

		self.owner_id = owner_id
		self.college = college
		self.matric_id = matric_id
		self.year = year
		self.student_id = student_id

	def get_student_data(self):

		my_cursor = mydb.cursor(buffered=True)

		my_cursor.execute("SELECT * FROM Student WHERE owner_id=" + str(self.owner_id))

		rowcount = my_cursor.rowcount

		if rowcount > 0:
			for row in my_cursor:
				self.student_id = row[0]
				self.college = row[1]
				self.matric_id = row[2]
				self.year = row[3]

	def insert_student_data(self, owner_id):

		my_cursor = mydb.cursor(buffered=True)

		self.vehicle.insert_vehicle_data(owner_id)

		sql = "INSERT INTO Student (owner_id, matric_id, college, year) VALUES (%s, %s, %s, %s)"
		val = (owner_id, self.matric_id, self.college, int(self.year))
		my_cursor.execute(sql, val)
		mydb.commit()

	def get_matric_id(self):
		return self.matric_id

	def get_college(self):
		return self.college

	def get_year(self):
		return self.year








