def countNumbers(x):
 summa = 0
 for simbols in x:
   summa = summa + int(simbols)
 return summa
x = input("Ievadiet skaitli: " )
rez = countNumbers(x)
print(rez)
 
