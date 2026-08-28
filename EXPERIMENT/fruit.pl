fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grapes, green).
fruit_color(mango, yellow).

show_fruits :-
    fruit_color(Fruit, Color),
    write(Fruit),
    write(' is '),
    write(Color),
    nl,
    fail.

show_fruits.