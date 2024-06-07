from faker import Faker
fake = Faker(["en_IN"])
for i in range(10):
    print("user name : ",fake.user_name())
    print("Host Name : ",fake.hostname())
    print("Doamin  Name : ",fake.domain_name())
    print("TLD : ",fake.tld())
    print("url : ",fake.url())
    print("uri : ",fake.uri())
    print("uri extension : ",fake.uri_extension())
    print("uri path : ",fake.uri_path())
    print("Slug : ",fake.slug())
    print("Image url : ",fake.image_url())
    print("requst Method",fake.http_method())
    