%kwadrat_lista(L1,L2)- spełniony gdy elementy listy L2 sa odpowiednimi elementami listy L1 podniesionymi do kwadratu.

kwadrat(X,Y):-Y is X*X.

kwadrat_lsita(L1,L2):-maplist(kwadrat,L1,L2).