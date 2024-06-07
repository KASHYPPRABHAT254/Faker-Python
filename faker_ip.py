from faker import Faker
fake = Faker()
for i in range(10):
    print("IPv4 : ",fake.ipv4())
    print("IPv6 : ",fake.ipv6())
    print("IPv4 Private : ",fake.ipv4_private())
    print("IPv4 Public : ",fake.ipv4_public())
    #print("IPv6 Private : ",fake.ipv6_private())
    #print("IPv6 Public : ",fake.ipv6_public())
    print("port Number : ",fake.port_number())
    print("MAC Address",fake.mac_address())