from pprint import pprint

from faker import Faker


users = []
fake = Faker('uk_UA')
for _ in range (25):
        users.append({"name":fake.name(), "birthday":fake.date_between('-50y','-30y')})
    
pprint(users)



