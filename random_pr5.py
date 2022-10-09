import random  

n=int(input("Dati numarul de elemente: "))
A=[]
for i in range(n):
    A.extend([random.randint(1,100)])
s=sum(A)-max(A)

print("Elementul maxim este:",max(A))
print("Tabloul A generat este:",A)
print("Suma elementelor mai mici ca elementul maxim este:",s)