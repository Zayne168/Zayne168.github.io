
% Zayne Bonner

eat(shark, fish).
eat(bear, fish).
eat(fish, algae).
eat(fox, rabbit).
eat(rabbit, grass).
eat(horse, grass).
eat(human, fish).
eat(wolf, bear).
eat(bird, worm).
eat(cat, bird).
eat(coyote, cat).


prey(X,Y):-
	eat(Y,X).

predator(X,Y):-
	eat(X,Y).

inTheFoodChain(X,Y):- eat(Y,X).
inTheFoodChain(X,Y):- eat(Y,Z), inTheFoodChain(X,Z).

commonPrey(X,Y,Z):- eat(X,Z), eat(Y,Z).

compete(X,Y):- commonPrey(X,Y,Z).


count([],0).
count([H|T], S) :- not(is_list(H)), count(T, S1), S is S1+1.
count([H|T], S) :- is_list(H), count(T, S1), count(H, S2), S is S1+S2.

% raise([], []).
% raise([H|T], [H2|T2]) :- H2 is (H+H*.0001+H*.01+H*.01),raise(T, T2).
% Above is my original implementation before it clicked what you meant by raise by percent. does the same thing 

raise([], []).
raise([H|T], [H2|T2]) :- H2 is (((H*1)*1.01)*1.01),raise(T, T2). % I hope that by 0% u meant .01 %

insert(E,[],[E]).
insert(E,[H|T],[H|T]):- E =:= H.
insert(E,[H|T],[E,H|T]):- E < H.
insert(E,[H|T],[H|L2]):- E > H, insert(E,T,L2).

delete(E,[],[]).
delete(E,[H|T],L2):- E =:= H, delete(E,T,L2).
delete(E,[H|T],[H|L2]):- E=\=H, delete(E,T,L2).