from  faker import Faker
fake = Faker()
for i in range(10):
    #print("job post : ",fake.job())
    print("company name : ",fake.company())
    print("company slogen : ",fake.bs())
    print("company Phrase : ",fake.catch_phrase())
    print("company Suffix : ",fake.company_suffix() )