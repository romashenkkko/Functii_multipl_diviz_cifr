import random

s=0
while True:
    a=random.randint(1,6)
    b=random.randint(1,6)
    s=a+b
    if (a==b):
        print("Dubla este:",a)
        break
print("Suma dublei este:",s)