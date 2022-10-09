import random
n=random.randint(1,999999999)
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a10=0

print("Numarul generat:",n)

while n>0:
    r=n%10
    n//=10
    if r==0:
        a1+=1
    elif r==1:
        a2+=1
    elif r==2:
        a3+=1
    elif r==3:
        a4+=1
    elif r==4:
        a5+=1
    elif r==5:
        a6+=1
    elif r==6:
        a7+=1
    elif r==7:
        a8+=1
    elif r==8:
        a9+=1
    elif r==9:
        a10+=1

print("Cifra 0 s=a regasit de",a1,"ori.")
print("Cifra 1 s=a regasit de",a2,"ori.")
print("Cifra 2 s=a regasit de",a3,"ori.")
print("Cifra 3 s=a regasit de",a4,"ori.")
print("Cifra 4 s=a regasit de",a5,"ori.")
print("Cifra 5 s=a regasit de",a6,"ori.")
print("Cifra 6 s=a regasit de",a7,"ori.")
print("Cifra 7 s=a regasit de",a8,"ori.")
print("Cifra 8 s=a regasit de",a9,"ori.")
print("Cifra 9 s=a regasit de",a10,"ori.")