import numpy as np
# #inicjalizacja tablicy
# a = np.arange(2)
# print(a)
# #lub drugi sposób
# a = np.array([0,1])
# print(a)
# #wypisanie typu zmiennej tablicy(nie jej elementow) - ndarray
# print(type(a))
# #sprawdzenie typu danych tablicy
# print(a.dtype)
# #inicjalizacja tablicy z konkretym typem danych
# a = np.arange(2, dtype = 'int64')
# print(a.dtype)
# #zapisywanie kopii tablicy jako tablicy z innym typem
# b = a.astype('float')
# print(b)
# print(b.dtype)
# #wypisywanie rozmiary tablicy
# print(b.shape)
# # mozna tez sprawdzic ilosc wymiarów tablicy
# print(a.ndim)
# #stworzenie tablicy wielowymiarowej moze wygladac tak
# #parametrem przekazywanym do funkcji array jest obiekt, który
# #zostanie skonwertowany na tablicę
# # moze być to Pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# #ponownie typem jest ndarray
# print(type(m))


#mozemy w łatwy sposób stworzyc macierz danego rozmiaru wypełniona zerami lub jedynkami
zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)
#można równierz stworzyc pustą macierz o podanych wymiarach, która pusta wcale nie jest
#wartości uieszczane są losowe, najpier podawana jest ilosc
#wierszy tablicy, potem ilosc kolumn
pusta = np.empty((2,2))
print(pusta)
#do elementów tablicy można odwołac się tak jak do elementów
#np. listy czyli podajac indeksy
poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_2)
print(poz_1)
#tworzenie macierzy 2x2 wraz z uzupełnieniem
macierz = np.array([[1,2],[3,4]])
print(macierz)
#funkcja arange potrafi także tworzyc ciągi liczb zmiennoprzecinkwoych
liczby = np.arange(1,2,0.1)
print(liczby)
#podonie działa funkcja linspace, której działanie jest równoważne funkci w MATLAB-ie
liczby_lin = np.linspace(1,2,5)
print(liczby_lin)
#a teraz możemy utworzyc dwie macierze, najpierw wartości
#iterowane sa w kolumnie a następnie w wierszu
z = np.indices((5,3))
print(z)
#wielowymiarowe macierze możemy równiez generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)
#podobnie jak w MATLAB-ie możemy tworzyc macierze diagonalne
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
#w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na głównej przekątnej macierzy
#możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej
#która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(4)],-1,)
print(mat_diag_k)
#Numpy jest wstanie stworzyć tablicę jednowymiarową z dowolego obiektu iterowalnego(iterable)
z = np.fromiter(range(5),dtype='int32')
print(z)
#ciekawą funkcja Numpy jest funkcja frombuffer, dzieki której mozęmy stworzyc np. tablice znaków
marcin = b'Marcin'
mar = np.frombuffer(marcin,dtype='S1')
print(mar)
mar_2 = np.frombuffer(marcin,dtype='S2')
print(mar_2)
#powyższa funkcja ma jednak pewną wadę dla pythona 3.x, która
#powodóje, że trzeba jawnie określić
#iż ciąg znaków przekazujemy jako ciąg bajtów co osiągamy po przez podanie litery 'b' przed wartością
#zmiennej tekstowej. Można podobne efekty osiągnąć inaczej
marcin = 'Marcin'
mar_3 =np.array(list(marcin))
mar_4 = np.array(list(marcin), dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin,dtype='S1')
mar_7 = np.fromiter(marcin,dtype='U1')
print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)
#talice w Numpy możemy w prosty sposób do siebie dodawać, odejmować, mnożyć, dzielić
mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)

a =np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
s = range(2,7,2)
#możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)
print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])
#w podobny sposób postępujemy w przypadku tablic wielowymiarowych
mat1 = np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierz 5x5
mat1 = mat1.reshape((5,5))
print(mat1)
print(mat1[1:])#od drugiego wiersza
print (mat1[:,1])#druga kolumna jako wektor
print(mat1[:,-1:]) #ostatnia kolumna
print(mat1[2:6, 1:3]) # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat1[:, range(2,6,2)]) # 3 i 5 kolumna
print('')
#bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcia można osiągnąć wg. poniższego przykładu
#y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows,cols]
print(y)
