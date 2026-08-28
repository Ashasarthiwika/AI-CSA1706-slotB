% Planet Database

planet(mercury, 1, terrestrial).
planet(venus, 2, terrestrial).
planet(earth, 3, terrestrial).
planet(mars, 4, terrestrial).
planet(jupiter, 5, gas_giant).
planet(saturn, 6, gas_giant).
planet(uranus, 7, ice_giant).
planet(neptune, 8, ice_giant).

% Find position and type of a planet

planet_details(Name, Position, Type) :-
    planet(Name, Position, Type).

% Find planet at a particular position

planet_at_position(Position, Name) :-
    planet(Name, Position, _).

% Find planets of a particular type

planets_by_type(Type, Name) :-
    planet(Name, _, Type).

% Display all planets

display_all :-
    planet(Name, Position, Type),
    write(Name), write(' - '),
    write(Position), write(' - '),
    write(Type), nl,
    fail.

display_all.