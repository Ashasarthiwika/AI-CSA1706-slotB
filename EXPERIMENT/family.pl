% Family Tree Database

% Parent facts
parent(john, alice).
parent(john, bob).
parent(mary, alice).
parent(mary, bob).

parent(bob, charlie).
parent(susan, charlie).

parent(bob, david).
parent(susan, david).

% Male and Female
male(john).
male(bob).
male(charlie).
male(david).

female(mary).
female(alice).
female(susan).

% Father
father(Father, Child) :-
    male(Father),
    parent(Father, Child).

% Mother
mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

% Child
child(Child, Parent) :-
    parent(Parent, Child).

% Sibling
sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.

% Grandparent
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

% Grandchild
grandchild(Grandchild, Grandparent) :-
    grandparent(Grandparent, Grandchild).

% Display all parent relationships
display_all :-
    parent(Parent, Child),
    write(Parent),
    write(' -> '),
    write(Child),
    nl,
    fail.

display_all.