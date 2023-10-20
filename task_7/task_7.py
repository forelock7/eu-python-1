# # Task 7.1
# from datetime import datetime
#
# file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_7/today.txt"
# now = datetime.today()
# with open(file_path, 'wt') as file:
#     file.write(str(now))
#
# with open(file_path, 'rt') as file:
#     today_string = file.read()
#
# print("today_string =", today_string)
# today = datetime.strptime(today_string, "%Y-%m-%d %H:%M:%S.%f")
# print("datetime:", today)
# print("year:", today.year)
# print("month:", today.month)
# print("day:", today.day)
# print("hour:", today.hour)
# print("minute:", today.minute)
# print("second:", today.second)
# print("microsecond:", today.microsecond)

# Task 7.2
from datetime import datetime
from datetime import timedelta
file_path = "/Users/volodymyrchubenko/Documents/Mine/Education/Repos/eu-python-1/task_7/poll.txt"
class Human():
    def __init__(self, birth_day):
        self.birth_day = datetime.strptime(birth_day, "%d.%m.%Y")

happy = Human("16.06.1986")
birth_date = happy.birth_day.date()
birth_week_day = happy.birth_day.strftime('%A')
number_of_days = 13330
spec_date = happy.birth_day + timedelta(days=number_of_days)


with open(file_path, 'wt') as file:
    print(f"What's your birthday?: {birth_date}", file=file, sep='\n')
    print(f"What day of the week were you born on?: {birth_week_day}", file=file, sep='\n')
    print(f"When will you be {number_of_days} days since birth?: {spec_date.date()}", file=file, sep='\n')