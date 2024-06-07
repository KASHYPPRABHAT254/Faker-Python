from faker import Faker
fake = Faker()
for i in range(10):
    print("fake md5 : ",fake.md5())
    print("fake sha1",fake.sha1())
    print("uuid : ",fake.uuid4())