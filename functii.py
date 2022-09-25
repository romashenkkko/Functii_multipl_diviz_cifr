import math
#1a
def nr_max(a,b,c):
    l=[a,b,c]
    max=0
    for numar in l:
        if numar>max:
            max = numar
    return max

#2b
def nr_min(a,b,c):
    l=[a,b,c]
    min=a
    for numar in l:
        if numar<min:
            min = numar
    return min

#3c
def c_m_mare_div(a,b,c):
    c_m_mare_div=0
    i=nr_min(a,b,c)
    while(i>1):
        if(a%i==0 and b%i==0 and c%i==0):
            c_m_mare_div = i
            break
        i-=1
    if(i<=1):
        c_m_mare_div = "Cel mai mare divizor comun este: 1"
        return print(c_m_mare_div)
    return print("Cel mai mare divizor comun al numerelor este: ",c_m_mare_div)

#4d
def c_m_mic_multiplu(a,b,c):
    i=nr_max(a,b,c)
    while True:
        if(i%a==0) and (i%b==0) and (i%c==0):
            multip= i
            break
        i+=1
    return print("Cel mai mic multiplu comun al numerelor este: ",multip)

#5e
def divizorii_comuni_3nr(a,b,c):
    at=[]
    bt=[]
    ct=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    for k in range (1,c+1):
        if (c%k==0):
            ct.append(k)
    d=set(at).intersection(bt)
    e=set(d).intersection(ct)
    br=list(e)
    return print("Toti divizorii comuni ai numerelor sunt: ",br)

#6f
def mult_com_cm_mici_primii_3(a,b,c):
    c_m_m_m=[]
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while len(c_m_m_m)<3:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return print("Primii 3 multipli comuni al numerelor  sunt: ",c_m_m_m)

#7g
def lat_triunghi(a,b,c):
    #import math#
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),2)
        perimetru=sp*2
        return print("Laturile pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    else:
        return print("Laturile date nu pot forma un triunghi!")

#8h
def ech_grad_2(a,b,c):
    #import math
    delta=((b**2)-(4*(a*c)))
    if delta>0:
        rad_delta=math.sqrt(int(delta))
        x1=round((-b-rad_delta)/(2*a),2)
        x2=round((-b+rad_delta)/(2*a),2)
        return print("Solutiile ecuatiei sunt: ",x1,"si",x2)
    elif delta==0:
        rad_delta=math.sqrt(int(delta))
        x1=x2=round((-b)/(4*a),2)
        return print("Solutiile sunt egale si valoarea lor este: ",x1)
    elif delta<0:
        return print("Ecuatia nu are solutii reale.")


x=int(input("Dati I-ul nr: "))
y=int(input("Dati II-a nr: "))
z=int(input("Dati III-a nr: "))

#1
print("Cel mai mic numar este:",nr_min(x,y,z))
#2
print("Cel mai mare numar este:",nr_max(x,y,z))
#3
(c_m_mare_div(x,y,z))
#4
(c_m_mic_multiplu(x,y,z))
#5
(divizorii_comuni_3nr(x,y,z))
#6
(mult_com_cm_mici_primii_3(x,y,z))
#7
(lat_triunghi(x,y,z))
#8
(ech_grad_2(x,y,z))