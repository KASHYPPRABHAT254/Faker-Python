from faker import Faker
fake = Faker(["en_IN"])
for i in range(10):
    print("Full Name: ",fake.name())
    print("Male Name: ",fake.name_male())
    print("Female Name: ",fake.name_female())
    print("Prefix: ",fake.suffix())