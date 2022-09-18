#1a
def suma(a,b):
    try:
        c=a+b
        return print("a) Suma numerelor ",a," si ",b," este: ",c)
    except:
        a,b= int(input('dati o valoare: '))


#2b
def produsul(a,b):
    c=a*b
    return print("b) Produsul numerelor ",a," si ",b," este: ",c)

#3c
def media_aritmetica(a,b):
    c=(a+b)/2
    return print("c) Media aritmetica a numerelor ",a," si ",b," este: ",c)

#4d
def c_m_mare_div_comun(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    c=set(at).intersection(bt)
    h=max(c)
    return print("d) Cel mai mare divizor comun al numerelor ",a," si ",b," este: ",h)

#5e
def c_m_mic_multiplu_comun(a,b):
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while True:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m=multiplu
            break
        multiplu +=1
    return print("e) Cel mai mic multiplu comun al numerelor ",a," si ",b," este: ",c_m_m_m)

#6f
def nr_min(a,b):
    if a<b:
        return print("f) Numarul minim este: ",a)
    else:
        return print("f) Numarul minim este: ",b)

#7g
def nr_max(a,b):
    if a>b:
        return print("g) Numarul maxim este: ",a)
    else:
        return print("g) Numarul maxim este: ",b)

#8h
def suma_nedef():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return print("h) ",a," + ",b," = ",c)

#9i
def produs_nedef():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a*b
    return print("i) ",a," * ",b," = ",c)
    
#10j
def divizorii_comuni(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    c=set(at).intersection(bt)
    br=list(c)
    return print("j) Toti divizorii comuni ai numerelor ",a," si ",b," sunt: ",br)

#11k 
def cinci_multipli_comuni(a,b):
    c_m_m_m=[]
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while len(c_m_m_m)<5:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return print("k) Cinci multipli comuni al numerelor ",a," si ",b," sunt: ",c_m_m_m)

#12l
def cifre_comune(a,b):
    aa=[]
    bb=[]
    for i in str(a):
        aa.append(int(i))
    for j in str(b):
        bb.append(int(j))
    c=set(aa).intersection(bb)
    br=list(c)
    if len(br)!=0:
        return print("l) Cifrele comune care se contin in numerele ",a," si ",b," sunt: ",br)
    else:
        return print("l) Numerele nu au cifre comune")

#13m
def dif_cif_num(a,b):
    aa=[]
    bb=[]
    for i in str(a):
        aa.append(int(i))
    for j in str(b):
        bb.append(int(j))
    c=set(aa).difference(bb)
    br=list(c)
    return print("m) Cifrele care se contin in numarul ",a," si nu se contin in numarul ",b," sunt: ",br)

#14n
def acelasi_nr_diviz(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    if len(at)==len(bt):
        return print("n) PRIETENE")
    else:
        return print("n) NU SUNT PRIETENE") 


q= int(input('a: '))
w= int(input('b: '))
#1
suma(q,w)
#2
produsul(q,w)
#3
media_aritmetica(q,w)
#4
c_m_mare_div_comun(q,w)
#5
c_m_mic_multiplu_comun(q,w)
#6
nr_min(q,w)
#7
nr_max(q,w)
#8
suma_nedef()
#9
produs_nedef()
#10
divizorii_comuni(q,w)
#11
cinci_multipli_comuni(q,w)
#12
cifre_comune(q,w)
#13
dif_cif_num(q,w)
#14
acelasi_nr_diviz(q,w)
