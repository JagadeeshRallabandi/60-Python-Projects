def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
s=input("Enter Temp in F")
p=convert(s)
print("Temp in C is",p)