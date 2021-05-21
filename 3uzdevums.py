
###Uzrakstiet programmu Python, 
#kas atgriezīs ar true vērtību, 
#ja divas norādītās veselu skaitļu vērtības
 #ir vienādas vai to summa vai starpība ir 5.
a=int(input("ievadiet pirmo skaitli: "))
b=int(input("ievadiet otro skaitli: "))
if a+b==5:
    print("true")
elif a-b==5:
    print("true")
elif b-a==5:
    print("true")
else:
    print("bop")

