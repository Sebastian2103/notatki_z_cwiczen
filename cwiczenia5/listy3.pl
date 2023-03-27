% lista_wieksza_o_1(L1,L2) - spełniony gdy elementy listy L2 są
% odpowiednimi elementami listy L1 powiększonymi o jednen.
% np. L1=[1,2,3] L2[2,3,4]


lista_wieksza_o_1([],[]).

%rekurencja:

lista_wieksza_o_1([H1|T1],[H2|T2):-
		H2 is H1+1,
		lista_wieksza_o_1(T1,T2).

