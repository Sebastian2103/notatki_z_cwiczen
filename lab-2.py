# a=9
# b=11
# if a>b:
#     print('liczba a jest wieksza od b')
# elif a<b:
#     print('liczba a jest mniejsza od b')
# else:
#     print('liczba a jest rowna liczbie b')


# print (a)
# print(type(a))
# a=int(a)
# print(type(a))
# a= input("wpisz pierwszą liczbę: ")
# b= input("wpisz drugą liczbę: ")
# c= input("wpisz trzecią liczbę: ")
# d= input("wpisz czwartą liczbę: ")
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# if (a>b)&(c>d):
#     print('liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d')
# else:
#     print('liczba a jest mniejsza od liczby b, lub liczba c jest mniejsza od liczby d')

# for licznik in sekwencja:
#     instrukcja lub blok instrukcji
# else:
#     instrukcje po wykonaniu pętli for
#
# range(start, stop, step)bardzo podobnie jak w C++

# for a in range(0,7,1):
#     print(a);

# lista =['a',5,6,5.6]
# for a in lista:
#     print(a)
# else:
#     print('Wyświetlone zostały wszystkie elementy z listy')

# pętla while
#
#         while warunek:
#             instrukcja lub blok instrukcji gdy warunek jest spelniony
#         else:
#             instrukcja po pętli
# a=0
# while (a<10):
#     print(a)
#     a+=1

# lista= [4,6,9,5,7,2,3]
# liczba=input('Podaj liczbę: ')
# licznik=0
# while licznik<len(lista):
#     if int(liczba)-lista[licznik]==0:
#         print('liczba '+str(liczba)+'-'+str(lista[licznik])+"=0")
#         break
#     else:
#         licznik+=1
# else:
#     print('żadna z warrtosci nie dała odpowiedniego wyniku')

# lista1=[4, 6, 8, 2, 3, 9]
# lista2=[4, 7, 5, 2]
# suma=[]
#
# for a in lista1:
#     for b in lista2:
#         wynik=a+b
#         suma.append(wynik)
#     print(suma)

# try:
#     instrukcje, ktore moga zawierac blad
#     albo tu wyniki gdy nie ma bledu
# except nazwa bledu 1:
#     instrukcja po wykryciu bledu1
# except nazwa bledu 2:
#     instrukcja po wykryciu bledu2
#     .
#     .
#     .
# else:
#     wyniki gdy nie ma bledu

# a = input('wczytaj pierwsza liczbe: ')
# b = input('wczytaj druga liczbe: ')
#
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a / b
#     print(wynik)
# except ZeroDivisionError:
#     print('Nie można dzielic przez 0')
# except ValueError:
#     print('Nie wczytano liczby całkowitej')

# KONTENERY DANYCH
# lista=['a',5,5.5,[1,2,3]]
# słownik={klucz:wartość}
# klucz w slowniku musi byc unikatowy
# a=lista[nr_indeksu]
# print(słownik[klucz])
#
# slownik={1:20,2:40}

# dodawanie do listy
# apped, insert,extand
# odejmowanie od listy
# pop, remove,del,
# sort,reverse

# lista=[6,7,8,1,2]
# lista.append(9)
# list.remove("50") # dany element
# lista.sort()
# lista.reverse()
#
# for a in lista:
#     print(a)

# dict={'model':'mustang', 'przebieg':'duzy'}
# dict.update({'kolor':'zielony'})
# dict.pop("model")
# for a in dict:
#     print(a)

