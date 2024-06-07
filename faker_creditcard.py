from faker import Faker
fake  = Faker()
for i in range(10):
    print("expire date : ",fake.credit_card_expire())
    print("credit card expiry details : ",fake.credit_card_full())
    print("credit card provider : ",fake.credit_card_provider())
    print("credit card number : ",fake.credit_card_number())
    print("credit card by provider :",fake.credit_card_number(card_type="maestro"))
    print("credit card CVV number : ",fake.credit_card_security_code())