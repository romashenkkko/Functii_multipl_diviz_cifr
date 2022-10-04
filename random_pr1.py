import random
n=int(input("Dati un  nr: "))
s_p=0
s_n=0
nr=[]
for x in range (n):
    k=random.randint(-30,50)
    nr.append(k)
    if k>0:
        s_p=s_p+k
    elif k<0:
        s_n=s_n+k

print("Numerele generate sunt:",nr)
if s_p==0:
    print("Nu au fost generate nr. pozitive.")
elif s_p!=0:
    print("Suma numerelor pozitive este:",s_p)
if s_n==0:
    print("Nu au fost generate nr. negative.")
elif s_n!=0:
    print("Suma numerelor negtive este:",s_n)