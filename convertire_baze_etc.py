#1
def cifra_maxima(n):
    max=0
    while n>0:
        r=n%10
        n//=10
        if r>max:
            max=r
    return max

def verificare_baza(n,b):
    elem=cifra_maxima(n)
    if elem<(b):
        return True
    else:
        return False
    
#2
def baze_necunoscute_in_baza_10(n,b):
        i=0
        s=0
        while n>0:
            r=n%10
            k=r*(b**i)
            n//=10
            s=s+k
            i=i+1
        return s

def suma_2_baze_10(a,q,b):
    aa=baze_necunoscute_in_baza_10(a,b)
    bb=baze_necunoscute_in_baza_10(q,b)
    c=aa+bb
    return c

def convertirea_din_baza_10_in_alta_adunarea(a,q,b):
    sum=suma_2_baze_10(a,q,b)
    list=[]
    while sum>0:
        nr=sum//b
        k=sum-(b*nr)
        list.append(k)
        sum=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Suma numerelor",qn,"si",qm,"in baza",zb,"este:",final,'.')

#3
def diferenta_2_baze_10(a,q,b):
    aa=baze_necunoscute_in_baza_10(a,b)
    bb=baze_necunoscute_in_baza_10(q,b)
    if aa>bb:
        c=aa-bb
        return c
    elif bb>aa:
        c=bb-aa
        return c

def convertirea_din_baza_10_in_alta_scaderea(a,q,b):
    dif=diferenta_2_baze_10(a,q,b)
    list=[]
    while dif>0:
        nr=dif//b
        k=dif-(b*nr)
        list.append(k)
        dif=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Diferenta numerelor",qn,"si",qm,"in baza",zb,"este:",final,'.')

#4
def inmultirea_2_baze_10(a,q,b):
    aa=baze_necunoscute_in_baza_10(a,b)
    bb=baze_necunoscute_in_baza_10(q,b)
    c=aa*bb
    return c

def convertirea_din_baza_10_in_alta_inmultirea(a,q,b):
    inm=inmultirea_2_baze_10(a,q,b)
    list=[]
    while inm>0:
        nr=inm//b
        k=inm-(b*nr)
        list.append(k)
        inm=nr
    br=reversed(list)
    final=''.join(map(str,br))
    return print("Inmultirea numerelor",qn,"si",qm,"in baza",zb,"este:",final,'.')


qn=int(input("Dati I-ul numar intreg: "))
qm=int(input("Dati al II-a numar intreg: "))
zb=int(input("Dati baza numerelor: "))

if (zb>1) and (zb<10):
    print("Rezultatul verificarii bazei numarului",qn,"este:",verificare_baza(qn,zb))
    print("Rezultatul verificarii bazei numarului",qm,"este:",verificare_baza(qm,zb))
    if verificare_baza(qn,zb) and verificare_baza(qm,zb) :
        convertirea_din_baza_10_in_alta_adunarea(qn,qm,zb)
        convertirea_din_baza_10_in_alta_scaderea(qn,qm,zb)
        convertirea_din_baza_10_in_alta_inmultirea(qn,qm,zb)