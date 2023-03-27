% szescian listy (L1,L2) - spelnniony gdy elemenety listy2 
% sa odpowiednimi elementami listy 1 podniesionymi do potegi 3

szescian_listy([],[]).

szescian_listy([H1|T1],[H2|T2]):- H2 is H1^3,
			szescian_listy(T1,T2).
