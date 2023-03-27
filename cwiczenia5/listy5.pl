%liczba elem(L,N) spełniony gdy N jest liczba elementów listy L


liczba_elem([],0).

liczba_elem([_|T1],N):-
 	liczba_elem(T,N1),
		N is N1+1.