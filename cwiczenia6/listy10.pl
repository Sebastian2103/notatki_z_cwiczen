%wiekszy_od(X,Y),
%spełniony gdy Y jest wiekszy od X

wiekszy_od(X,Y):-Y>X.

%spełniony gdy wszystkie elementy listy L są wieksze od X

wiekszy_od_lista(X,L):-maplist(wiekszy_od(X),L).