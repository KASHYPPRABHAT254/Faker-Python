from faker import Faker
fake = Faker(["en_IN"])
for i in range(10):
    print("Phone Number : ",fake.phone_number())
    print("country calling code : ",fake.country_calling_code())
    print("MSISDN : ",fake.msisdn())
 