% Bird Database

bird(eagle).
bird(parrot).
bird(pigeon).
bird(crow).
bird(penguin).
bird(ostrich).
bird(emu).

can_fly(eagle).
can_fly(parrot).
can_fly(pigeon).
can_fly(crow).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(emu).

check_flight(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.').

check_flight(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.').

display_all :-
    bird(Bird),
    check_flight(Bird),
    nl,
    fail.

display_all.