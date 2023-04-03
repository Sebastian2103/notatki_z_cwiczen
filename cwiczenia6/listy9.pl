%dodatni

dodatni(X):-X>0.

%lista dodatnia(L) spełniony gdy wszystkie elementy listy są dodatnie

lista_dodatnia(L):-maplist(dodatni,L).