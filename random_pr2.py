import random 
n=round(random.random()*10)
lista=[]
for x in range(n):
    lista.append(random.randint(1,6))
    k=lista.count(6)
    
print("Numarul de aruncari ale zarului este:",n)
print("Fetele pe care au cazut zarul sunt:",lista)
if k==0:
    print("Fata cu cifra 6 nu a cazut nici o data.")
else:
    print("Fata cu cifra 6 se repeta de",k,"ori")