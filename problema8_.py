import math
#3
def mediane(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        ma=round(0.5*(math.sqrt((2*(b**2))+(2*(c**2))-(a**2))),3)
        mb=round(0.5*(math.sqrt((2*(a**2))+(2*(c**2))-(b**2))),3)
        mc=round(0.5*(math.sqrt((2*(b**2))+(2*(a**2))-(c**2))),3)
        return print("Mediana laturei a:",a, "este:",ma,"; mediana laturei b:",b, "este:",mb,"mediana laturei c:",c, "este:",mc)
    else:
        return print("Laturile date nu pot forma un triunghi!")

med_a=int(input("Dati numarul a: "))
med_b=int(input("Dati numarul b: "))
med_c=int(input("Dati numarul c: "))

(mediane(med_a,med_b,med_c))