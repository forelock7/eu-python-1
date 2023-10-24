from task_8.privileges import Privileges
from task_8.user import User


class Admin(User):
    def __init__(self, first_name, last_name, birthday, city):
        super().__init__(first_name, last_name, birthday, city)
        self.priv = Privileges()



# # Task 8.2c
# print("**** Task 8.2c ***")
# oleg = Admin("Oleg", "Petrenko", "31.06.2000", "Lviv")
# oleg.show_privileges()

# # Task 8.2d
# print("**** Task 8.2d ***")
# bogdan = Admin("Bogdan", "Kudo", "05.04.1995", "Kyiv")
# bogdan.priv.show_privileges()