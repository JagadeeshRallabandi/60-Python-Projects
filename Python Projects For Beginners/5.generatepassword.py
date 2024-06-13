import random
passlen=int(input("Enter length of password:"))
s="abcdefghijklmnopqrstuvwxyz!@#$%^&*(+_-)?"
p="".join(random.sample(s,passlen))
print(p)