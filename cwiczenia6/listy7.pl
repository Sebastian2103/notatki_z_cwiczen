%Sprawdza czy dany element jest elementem listy E jest w liscie L
%warunek kończący rekurencje
element(E,[E|_]).
%rekurencja: jezeli E jest elementem listy L,  a nie jest jej głową, to jest elemenrem ogona
	element(E,[_|T]):-element(E,T).
