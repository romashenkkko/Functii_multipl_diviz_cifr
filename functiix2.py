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
    return print("Cel mai mare divizor comun al numerelor ",a , b," si ", c," este: ",c_m_mare_div)

#4d
def c_m_mic_multiplu(a,b,c):
    i=nr_max(a,b,c)
    while True:
        if(i%a==0) and (i%b==0) and (i%c==0):
            multip= i
            break
        i+=1
    return print("Cel mai mic multiplu comun al numerelor ", a , b ," si ",c," este: ",multip)



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