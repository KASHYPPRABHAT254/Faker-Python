from faker import Faker
fake = Faker()
for i in range(10):
    print("currency: ",fake.currency())
    print("Currency Name : ",fake.currency_name())
    print("Currency Code : ",fake.currency_code())
    print("Cryptocurrency Name : ",fake.cryptocurrency_name())