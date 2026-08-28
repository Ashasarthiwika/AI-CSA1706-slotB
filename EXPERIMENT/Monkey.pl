% Monkey Banana Problem

% Initial state:
% monkey is at door
% box is at window
% bananas are at middle
% monkey is on floor

% Monkey can move from one place to another

move(monkey, X, Y) :-
    X \= Y,
    write('Monkey moves from '),
    write(X),
    write(' to '),
    write(Y),
    nl.

% Monkey pushes box

push_box(X, Y) :-
    write('Monkey pushes box from '),
    write(X),
    write(' to '),
    write(Y),
    nl.

% Monkey climbs on the box

climb_box :-
    write('Monkey climbs on the box'),
    nl.

% Monkey gets bananas

get_banana :-
    write('Monkey gets the bananas'),
    nl.

% Solution

solve :-
    move(monkey, door, window),
    push_box(window, middle),
    climb_box,
    get_banana.