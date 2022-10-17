from typing import List, Any
from typing import Dict, Any
#
# a: int = 7
#
#
# def suma(x: int, y: int = 9) -> int:
#     return x + y
#
#
# def pro() -> None:
#     print("abc")
#
#


def suma_macierzy(A: List[list[int]], B: List[list[int]]) -> List[List[int]]:
    temp = []
    for i in range(0, len(A)):
        temp2 = []
        for j in range(0, len(A[i])):
            temp2.append(A[i][j]+B[i][j])
        temp.append(temp2)
    return temp

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


lista: List[List[int]] = [[1,2],[1,2]]
lista1: List[List[int]] = [[2,1],[5,3]]
print(getMatrixInverse(lista1))


##posortowanie po kluczach

d1: Dict[str, int] = {"k1":34,"k2":2,"k0":11, "k3":63,"k4":21, "k5":43}
print(sorted(d1))
print(dict(sorted(d1.items())))
d1 = dict(sorted(d1.items()))

##Posortowanie po wartościach

sort_key = sorted(d1, key = d1.get)
d2: Dict[str, int] = {}
for elem in sort_key:
    d2[elem] = d1[elem]
d1= d2
print(d1)

