from faker import Faker
fake  = Faker()
for i in range(10):
    print("word : ",fake.word())
    print("Words : ",fake.words())
    print("Words : ",fake.words(nb = 5))
print("Text : ",fake.text())
print("Texts : ",fake.texts())
print("sentence : ",fake.sentence())
print("sentences : ",fake.sentences())