mniejszy(X,Y):-Y is X-1.

mniejszy_lista(L1,L2):-maplist(mniejszy,L1,L2).