from datetime import datetime, timedelta

users = [  {"name": "Petya",  "birthday": datetime(year=1990, month=11, day=15)},
           {"name": "Kostya", "birthday": datetime(year=1991, month=11, day=18)},
           {"name": "Serhiy", "birthday": datetime(year=1992, month=11, day=13)},
           {"name": "Sasha",  "birthday": datetime(year=1993, month=11, day=12)},
           {"name": "Nastya", "birthday": datetime(year=1994, month=11, day=24)},
           {"name": "Vasya",  "birthday": datetime(year=1990, month=11, day=13)},
           {"name": "Pasha",  "birthday": datetime(year=1980, month=11, day=14)},
           {"name": "Olia",   "birthday": datetime(year=2000, month=9, day=24)}]

def get_birthdays_per_week(some_list):
    current_date = datetime.today().date()
    next_week = [] # создает лист со следующими 7 днями
    for i in range(7):
        next_week.append(current_date + timedelta(days=i+1))
    birthday_dict = dict.fromkeys(next_week, '')
    for user in some_list:
        user_date = user.get("birthday").replace(year=current_date.year) # подменяем год рождления на текущий и смотрим попадает ли в нашу ближайшую неделю
        if user_date.date() in next_week:
            if birthday_dict[user_date.date()] > '':
                birthday_dict[user_date.date()] = birthday_dict[user_date.date()] + ', ' + user.get("name")
            else:
                birthday_dict[user_date.date()] = user.get("name")
    weekend_birthday_names = ''
    for key, value in birthday_dict.items():
        if key.weekday() == 5:
            weekend_birthday_names = value
        elif key.weekday() == 6:
            weekend_birthday_names = weekend_birthday_names + ', ' + value
        elif key.weekday() == 0:
            print(key.strftime('%A :'), weekend_birthday_names, ', ', value)
        else:
            print(key.strftime('%A :'), value)

if __name__ == "__main__":
    get_birthdays_per_week(users)
