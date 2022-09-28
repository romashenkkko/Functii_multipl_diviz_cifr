import math

#1
def triunghiuri(a,b,c,d):
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),3)
        perimetru=sp*2
        return print("Laturile",a,',',b,',',c, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    elif (a+b>d) and (a+d>b) and (b+d>a):
        sp=(a+b+d)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",a,',',b,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    elif (c+b>d) and (c+d>b) and (d+b>c):
        sp=(c+b+d)/2
        aria=round(math.sqrt(sp*(sp-c)*(sp-b)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",c,',',b,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)

    elif (c+a>d) and (c+d>a) and (d+a>c):
        sp=(c+a+d)/2
        aria=round(math.sqrt(sp*(sp-c)*(sp-a)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",c,',',a,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)


x=int(input("Dati I-ul nr: "))
y=int(input("Dati II-a nr: "))
z=int(input("Dati III-a nr: "))
q=int(input("Dati IV-a nr: "))

(triunghiuri(x,y,z,q))


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

#bzbzFINAL2
def min_max(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    S=max(min(a1,a2),max(a3,a4))+min(max(a5,a6),min(a7,a8))
    T=min(a1,a2)+min(a3,a4)+min(a5,a6)+min(a7,a8)+min(a9,a10)
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


#3
def mediane(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        ma=round(0,5*(math.sqrt((2*(b**2))+(2*(c**2))-(a**2))),3)
        mb=round(0,5*(math.sqrt((2*(a**2))+(2*(c**2))-(b**2))),3)
        mc=round(0,5*(math.sqrt((2*(b**2))+(2*(a**2))-(c**2))),3)
        return print("Mediana laturei a:",a, "este:",ma,"; mediana laturei b:",b, "este:",mb,"mediana laturei c:",c, "este:",mc)
    else:
        return print("Laturile date nu pot forma un triunghi!")

med_a=int(input("Dati numarul a: "))
med_b=int(input("Dati numarul b: "))
med_c=int(input("Dati numarul c: "))

(mediane(med_a,med_b,med_c))


#4
def inaltimea_trg(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),3)
        ha=round((2*aria)/a,3)
        hb=round((2*aria)/b,3)
        hc=round((2*aria)/c,3)
        return print("Inaltimea triunghiului pe latura",a,"este:",ha,"; pe latura",b,"este:",hb,", iar pe latura",c,"este:",hc,".")
    else:
        return print("Laturile date nu pot forma un triunghi!")


o=int(input("Dati I-ul nr: "))
p=int(input("Dati II-a nr: "))
r=int(input("Dati III-a nr: "))  

(inaltimea_trg(o,p,r))
