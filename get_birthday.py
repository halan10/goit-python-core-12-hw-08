from pprint import pprint

from faker import Faker
from datetime import datetime, timedelta,date
from collections import defaultdict

users = []
fake = Faker('uk_UA')
for _ in range (25):
        name_user = fake.name()
        date_birthday_user = str(fake.date_between('-50y','-30y'))
        users.append({"name":name_user, "birthday":date_birthday_user})
    
pprint(users)

def get_next_week_start(d:datetime):
        diff_days = (7-d.weekday())
        return d + timedelta(days=diff_days)

def prepare_birthday(text: str):
        bd = datetime.strptime(text, '%Y-%m-%d')
        return bd.replace(year=datetime.now().year).date()

def get_birthday_per_week(users):
        birthdays = defaultdict(list)
        today = datetime.now().date()
        next_week_start = get_next_week_start(today)
        start_period = next_week_start - timedelta(2)
        end_period = next_week_start + timedelta(4)
        print(f"\nThis week : {str(start_period), str(end_period)}")
        
        happy_users = [user for user in users if start_period <= prepare_birthday(user ['birthday']) <= end_period]
        if not happy_users:
                print('\nNo birthdays this week!')
        else:
                print("\nThis week we should congratulate:")
                pprint(happy_users)
                print("\nThis week it is worth congratulating on the following days:")

        for user in happy_users:
                
                current_bd = prepare_birthday(user['birthday'])
                if current_bd.weekday() in (5,6):
                        birthdays['Mondey'].append(user['name'])
                else:
                        birthdays[current_bd.strftime('%A')].append(user['name'])
                return birthdays

if __name__ == "__main__":
        result = get_birthday_per_week(users)
        pprint(result)