C=False
while C == False:
    n1=(input("enter first number: "))
    if "," in n1 :
        n1=n1.replace(",", ".")
        float(n1)
        print(n1)
        C=True
    else:
        C=True
o=input("pleas enter +;-;*;/ or ^: ")
n2=(input("enter second number: "))
if "," in n2 :
        n2=n2.replace(",", ".")
        float(n2)
        print(n2)
        C=True
checker=True
if "," in n1 :
    print("kein kommer")

n1=float(n1)
n2=float(n2)
if o == "+" :
    
    n1+=n2
    (print(n1))
    checker=False
if o == "-" :
    
    n1-=n2
    (print(n1))
    checker=False
if o == "*" :
    n1*=n2
    (print(n1))
    checker=False
if o == "^" :
    for i in range(0,n2):
        n1*=n1
    (print(n1))
    checker=False
if o == "/" :
    if n2 == 0:
        print("Division by 0 not possible")
        
    else:
        n1/=n2
        (print(n1))
        checker=False
else:
    if checker == True:
        print("Pleas only enter Numbers")
