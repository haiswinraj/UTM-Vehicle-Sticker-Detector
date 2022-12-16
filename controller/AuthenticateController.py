from model.Admin import Admin


class AuthenticateController:

    def login(self, username, password):
        admin = Admin(username, password)
        return admin.login()

    def signUp(self, username, password):
        admin = Admin(username, password)
        return admin.signUp()


