
jarosz(ola).
jarosz(ewa).
jarosz(jan).
jarosz(paweł).
nie_pali(ola).
nie_pali(ewa).
nie_pali(jan).
czyta(ola).
czyta(iza).
czyta(piotr).
sport(ola).
sport(jan).
sport(piotr).
sport(paweł).
lubi(ola,Y):-jarosz(Y),sport(Y).
lubi(ewa,Y):-nie_pali(Y),jarosz(Y).
lubi(iza,Y):-czyta(Y).
lubi(iza,Y):-nie_pali(Y),sport(Y).
lubi(jan,Y):-sport(Y).
lubi(piotr,Y):-sport(Y),jarosz(Y).
lubi(piotr,Y):-czyta(Y).
lubi(paweł,Y):-jarosz(Y),sport(Y),czyta(Y).