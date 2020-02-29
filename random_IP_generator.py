import random
octet = []
for i in range(4):
    octet.append(str(random.randint(0, 255)))
print(octet[0] + '.' + octet[1] + '.' + octet[2] + '.' + octet[3])
