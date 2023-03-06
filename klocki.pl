%PROGRAM: klocki_1
%Baza wiedzy o układzie klockółw
%Definiowane predykaty:
%      na/2
%============================
%klocek x lezy pomiędzy kolockami d i a

%na(X,Y)
%opis: spełniony, gdy klocek X leży bezpośrednio na klocku Y
%-----------------------------na/2
	na(c,a).
	na(c,b).
	na(d,c).
    pod(X,Y):-na(Y,X).
	miedzy(X,Y,Z) :-na(X,Y),pod(X,Z).
	miedzy(X,Y,Z) :-na(X,Z),pod(X,Y).
%-----------------------------na/2
/*nasz program składa sie z 6 klauzul
program składa sie z 3 definicji relacji (na, pod między)
mamy 3 fakty(te na to fakty) i z 3 reguł (pod,miedzy,miedzy).
*/
