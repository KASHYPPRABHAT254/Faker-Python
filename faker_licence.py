from faker import Faker
fake = Faker(["en_IN"])
for i in range(10):
    print("Vehical License Plate number : ",fake.license_plate())