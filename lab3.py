import math
# lista=[]
# for element in sekwencja:
#     warunek_na_element:
#     appdend(akcja_na_element)
#
# list=[akcja_na_element for element in selwencja if warunek_na_element]
# a=[]
# lista =[]
# for x in range(0,10):
#     a.append(x**2)
# print(a)
# a2=[x**2 for x in range(0,10)]
# print(a2)
# b=[]
# for x in range(0,6):
#     b.append(3**x)
# print(b)
# b2=[3**x for x in range(0,6)]
# print(b2)
# c=[]
# for x in a:
#     if(x%2==1):
#         c.append(x)
# print(c)
# c2=[]
# c2=[x for x in a if x%2==1]
# print(c2)
# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a, b))
# print(lista)
# lista2 = [(a, b)for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik = {'PZU':'Państwowy zakład ubepieczeń',
#            'ZUS':'Zakład ubepieczeń społecznych',
#            'PKO':'Państwowa kasa oszczędności'}
# print(slownik)
# slownik_odwrocony = {}
# for key,value in slownik.items():
#     slownik_odwrocony[value]=key
# print(slownik_odwrocony)
# slowink2={value: key for key, value in slownik.items()}
# print(slowink2)

################################
            #Funkcje
# def nazwa_funkcji(arg.pozycyjne, domyślna=warotść, *argument, **argument):
# insttrukcje
# return

# def row_kwadratowe(a,b,c):
#     delta=b**2-4*a*c
#     if(delta<0):
#         print('Brak rozwiązan')
#         return -1
#     elif delta==0:
#         print('Jedno rozwiązanie')
#         x=(-b)/(2*a)
#         return x
#     else:
#         print('Ma dwa rozwiązania')
#         x1 = ((-b)-math.sqrt(delta)/(2*a))
#         x2 = ((-b) + math.sqrt(delta) / (2 * a))
#         return x1, x2
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2,1))
# print(row_kwadratowe(1,4,1))

# def parzystosc(a):
#     if (a%2==0):
#         print('Liczba jest parzysta')
#         return a
#     else:
#         print('Liczba jest nieparzysta')
#         return a
# parzystosc(1234125351)

# def dlugosc_odcinka(x1=1,y1=2,x2=3,y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# #argumenty z wartościami domyślnymi
# print(dlugosc_odcinka())
# #argumenty z wartościami pozycyjnymi
# print(dlugosc_odcinka(4,1,6,7))
# #dwa pierwsze argumenty pozycyjne reszta z nowa wartoscia
# print(dlugosc_odcinka(1,1,y2=8,x2=7))
# #wszystkie z nowa wartoscia
# print(dlugosc_odcinka(y2=3,x1=5,x2=0,y1=6))
# #dwa pierwsza jako domyslne resza z nowa wartoscia
# print(dlugosc_odcinka(y2=1,x2=6))

# def ciag(* liczba):
#     if len(liczba)==0:
#         return 0
#     else:
#         suma = 0
#         for i in liczba:
#             suma += i
#         return suma
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8))

# def co_lubie(**rzeczy):
#     for cos in rzeczy:
#         print('lubie')
#         print(cos)
#         print('co jest')
#         print(rzeczy[cos])
# 
# co_lubie(gry=['planszowe','komputerowe'])
