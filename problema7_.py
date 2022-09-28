#2
def max(a,b):
    l=[a,b]
    max=0
    for numar in l:
        if numar>max:
            max = numar
    return max

def min(a,b):
    l=[a,b]
    min=a
    for numar in l:
        if numar<min:
            min = numar
    return min

#bzbzFINAL
def min_max(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    S=max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8))
    T=min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)+max(a1,a2)+max(a3,a4)+max(a5,a6)+max(a7,a8)+max(a9,a10)
    return print ("S=",S,", iar T=",T)

e=int(input("Dati I-ul nr: "))
f=int(input("Dati II-a nr: "))
g=int(input("Dati III-a nr: "))
h=int(input("Dati IV-a nr: "))
i=int(input("Dati V-a nr: "))
j=int(input("Dati VI-a nr: "))
k=int(input("Dati VII-a nr: "))
l=int(input("Dati VIII-a nr: "))
m=int(input("Dati IX-a nr: "))
n=int(input("Dati X-a nr: "))

(min_max(e,f,g,h,i,j,k,l,m,n))
