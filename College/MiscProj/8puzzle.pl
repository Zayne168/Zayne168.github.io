% Zayne Bonner 800756759
% format= eightPuzzle([1,2,3,4,5,6,0,7,8],[1,2,3,4,0,5,6,7,8],SP).
% a limited DFS was implemented due to the dfs getting stuck in a state of an infinite loop 
% the max depth is set at 20 currently, but can be increased as needed or decreased,

move(Cur, Next) :- up(Cur, Next);
					down(Cur,Next); 
					left(Cur,Next);
					right(Cur,Next).


up([A, B, C, 0, D, E, F, G, H], [0, B, C, A, D, E, F, G, H]).
up([A, B, C, D, 0, E, F, G, H], [A, 0, C, D, B, E, F, G, H]).
up([A, B, C, D, E, 0, F, G, H], [A, B, 0, D, E, C, F, G, H]).
up([A, B, C, D, E, F, 0, G, H], [A, B, C, 0, E, F, D, G, H]).
up([A, B, C, D, E, F, G, 0, H], [A, B, C, D, 0, F, G, E, H]).
up([A, B, C, D, E, F, G, H, 0], [A, B, C, D, E, 0, G, H, F]).

down([0, A, B, C, D, E, F, G, H], [C, A, B, 0, D, E, F, G, H]).
down([A, 0, B, C, D, E, F, G, H], [A, D, B, C, 0, E, F, G, H]).
down([A, B, 0, C, D, E, F, G, H], [A, B, E, C, D, 0, F, G, H]).
down([A, B, C, 0, D, E, F, G, H], [A, B, C, F, D, E, 0, G, H]).
down([A, B, C, D, 0, E, F, G, H], [A, B, C, D, G, E, F, 0, H]).
down([A, B, C, D, E, 0, F, G, H], [A, B, C, D, E, H, F, G, 0]).


left([A, 0, B, C, D, E, F, G, H], [0, A, B, C, D, E, F, G, H]).
left([A, B, 0, C, D, E, F, G, H], [A, 0, B, C, D, E, F, G, H]).
left([A, B, C, D, 0, E, F, G, H], [A, B, C, 0, D, E, F, G, H]).
left([A, B, C, D, E, 0, F, G, H], [A, B, C, D, 0, E, F, G, H]).
left([A, B, C, D, E, F, G, 0, H], [A, B, C, D, E, F, 0, G, H]).
left([A, B, C, D, E, F, G, H, 0], [A, B, C, D, E, F, G, 0, H]).

right([0, A, B, C, D, E, F, G, H], [A, 0, B, C, D, E, F, G, H]).
right([A, 0, B, C, D, E, F, G, H], [A, B, 0, C, D, E, F, G, H]).
right([A, B, C, 0, D, E, F, G, H], [A, B, C, D, 0, E, F, G, H]).
right([A, B, C, D, 0, E, F, G, H], [A, B, C, D, E, 0, F, G, H]).
right([A, B, C, D, E, F, 0, G, H], [A, B, C, D, E, F, G, 0, H]).
right([A, B, C, D, E, F, G, 0, H], [A, B, C, D, E, F, G, H, 0]).


 % SP = SolutionPath
  % had to set up a max depth in order to get the dfs to work without an infinite loop.
  eightPuzzle(Start, GoalState, SP) :- Depth is 20,dfs(Start, GoalState, SP, Depth),printEP(SP).
  % set up
  dfs(Start,GoalState,SP,Depth) :- 
  	dfs1(Start,GoalState,[Start],SP,Depth).
  
  % base case
  dfs1(Current,Goalstate,PathSoFar,SP,_) :- 
	 Goalstate=Current,
  	 reverse(PathSoFar,SP).
  
  % recursive case
  dfs1(Current, GoalState, PathSoFar, SP, Depth) 
  	:-  Depth>0,
			move(Current,Next), not(member(Next, PathSoFar)), 
				% if yes, we've been to Next, fail
		NewD is Depth -1,
			dfs1(Next,GoalState,[Next|PathSoFar],SP,NewD).
		
	% State being the current state at each step.
	printEP([]).
	printEP([State|T]) :-
		pmatrix(State),
		nl,  
		printEP(T).
	
	pmatrix([A, B, C, D, E, F, G, H, I]) :-
		write(A), write(' '), write(B), write(' '), write(C), nl,
		write(D), write(' '), write(E), write(' '), write(F), nl,
		write(G), write(' '), write(H), write(' '), write(I), nl.