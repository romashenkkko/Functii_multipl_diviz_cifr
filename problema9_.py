import math
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