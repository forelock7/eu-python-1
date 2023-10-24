class Privileges():
    def __init__(self):
        self.privileges = ['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users']

    def show_privileges(self):
        print(f"Privileges: {self.privileges}")