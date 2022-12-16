from controller.Database import mydb


class Admin():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT admin_id FROM Admin WHERE username='" + self.username + "' AND password='" + self.password + "'")
        rowcount = mycursor.rowcount

        return rowcount

    def signUp(self):
        mycursor = mydb.cursor(buffered=True)

        sql = "INSERT INTO Admin (username, password) VALUES (%s, %s)"
        val = (self.username, self.password)
        mycursor.execute(sql, val)
        mydb.commit()


