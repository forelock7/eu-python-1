class User:
    def __init__(self, first_name, last_name, birthday, city):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name)

    def greeting_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# # Task 8.2a
# print("**** Task 8.2a ***")
# vova = User("Volodymyr", "Chubenko", "01.01.1990", "Kyiv")
# vova.describe_user()
# vova.greeting_user()
#
# oleg = User("Oleg", "Petrenko", "31.06.2000", "Lviv")
# oleg.describe_user()
# oleg.greeting_user()

# # Task 8.2b
# print("**** Task 8.2b ***")
# bogdan = User("Bogdan", "Kudo", "05.04.1995", "Kyiv")
# bogdan.increment_login_attempts()
# bogdan.increment_login_attempts()
# bogdan.increment_login_attempts()
# print("login_attempts =", bogdan.login_attempts)
# bogdan.reset_login_attempts()
# print("login_attempts =", bogdan.login_attempts)
