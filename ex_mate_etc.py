def nr_cifre(a):
    nr=0
    while a>0:
        r=a%10
        a//=10
        nr=nr+1
    return print("Numarul de cifre este:",nr)

def nr_cifre_pare(a):
    l=[]
    while a>0:
        l.append(a%10)
        a//=10
    pare=[]
    for i in l:
        if i%2==0 :
            pare.append(i)
    z=len(pare)
    return print("Numarul de cifre pare este:",z)

def nr_cifre_impare(a):
    lst=[]
    while a>0:
        lst.append(a%10)
        a//=10
    imp=[]
    for i in lst:
        if i%2!=0 :
            imp.append(i)
    z=len(imp)
    return print("Numarul de cifre impare este:",z)

def suma_cifrelor(a):
    s=0
    while a>0:
        r=a%10
        a//=10
        s=s+r
    return print("Suma cifrelor este:",s)

def cifra_maxima(a):
    max=0
    while a>0:
        r=a%10
        a//=10
        if r>max:
            max=r
    return print("Cifra maxima este:",max)

def cifra_minima(a):
    min=9
    while a>0:
        r=a%10
        a//=10
        if r<min:
            min=r
    return print("Cifra minima este:",min)

def media_aritmetica_cifre(a):
    s=0
    lst=[]
    while a>0:
        r=a%10
        a//=10
        s=s+r
        lst.append(r)
        nr_cifre=len(lst)
        med_arit=s//nr_cifre
    return print("Media aritmetica a cifrelor este:",med_arit)

def cifre_care_se_repeta(a):
    lst=[]
    a=str(a)
    for i in a:
        if a.count(i)>=2:
            if i not in lst:
                lst.append(i)
    return print("Cifrele care se repeta de cel putin 2 ori sunt:", lst)

def cifre_separat(a):
    separ=str(a)[::1]
    lst=list(separ)
    z=' '.join(lst)
    return print("Cifrele afisate separat sunt",z)

def divizorii_nr(a):
    at=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    return print("Divizorii numarului",q," sunt:", at)

def inversul(a):
    nr_invers=0
    while a>0:
        cifra=a%10
        nr_invers=(nr_invers*10)+cifra
        a//=10
        at=str(nr_invers)
    return print("Inversul numarului",q, "este: ", at)

def c_m_mare_nr_din_cifre(a):
    at=[]
    while a>0:
        c=a%10
        at.append(c)
        a//=10
    at.sort(reverse=True)
    z="".join(str(i) for i in at)
    return print("Cel mai mare numar format din cifrele numarului",q,"este:",z)

def nr_prim(a):
    if a>1:
        for i in range (2,a):
            if (a%i==0):
                return print("Numarul",q,"nu este numar prim")
        return print("Numarul",q,"este numar prim")
    return print("Numerele prime incep de la 1 in sus!")
             


q= int(input('a: '))
if q<100000:
    (nr_cifre(q))
    (nr_cifre_pare(q))
    (nr_cifre_impare(q))
    (suma_cifrelor(q))
    (cifra_maxima(q))
    (cifra_minima(q))
    (media_aritmetica_cifre(q))
    (cifre_care_se_repeta(q))
    (cifre_separat(q))
    (divizorii_nr(q))
    (inversul(q))
    (c_m_mare_nr_din_cifre(q))
    (nr_prim(q))
else:
    print("Numarul e mai mare ca 100000!")