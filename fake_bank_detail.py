from faker import Faker
fake = Faker(["en_IN"])
print("Bank ABA Transit number : ",fake.aba())
print("Bank Country : ",fake.bank_country())
print("Basic Bank account No. : ",fake.bban())
print("International Basic Bank account number : ",fake.iban())
print("Swift Bank Account Number : ",fake.swift(length  = 11))
