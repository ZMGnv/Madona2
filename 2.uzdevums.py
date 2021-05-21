 
#Uzrakstīt programmu Python, lai
#atņemot divus norādītos veselos skaitļus. 
#Tomēr, ja starpībs vērtība ir mazāka kā 10 un lielāka kā -10, 
#atgriezt tekstu Poga.

from math import *
a=int(input("ievadiet pirmo skaitli: "))
b=int(input("ievadiet otro skaitli: "))
c=a-b
if c>-10:
    c<10
    print("poga")
else:
    print("ok")
