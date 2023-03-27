%lista razy 3 - spełniony gdy elementy listy L2 sa odpowiednimi elemenetami listy L1 pomnożonymi przez 3

lista_razy_3([],[]).

%rekurencja

lista_razy_3([H1|T1],[H2|T2]):- H2 is H1*3,
    lista_razy_3(T1,T2).
