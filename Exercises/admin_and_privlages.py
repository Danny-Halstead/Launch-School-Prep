from user import User

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privlages = Privlages()

class Privlages():
    def __init__(self):
        self.privlages = ['ban', 'delete', 'mute']

    def show_privlages(self):
        print(f'Users with privlages can {self.privlages}')