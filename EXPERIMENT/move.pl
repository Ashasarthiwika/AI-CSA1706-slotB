move(state(middle, on_floor, middle, has_not),
     grasp,
     state(middle, on_floor, middle, has)).

move(state(P, on_floor, P, Has),
     climb,
     state(P, on_box, P, Has)).

move(state(P, on_floor, B, Has),
     walk(P, B),
     state(B, on_floor, B, Has)).

move(state(P, on_floor, B, Has),
     push(P, B),
     state(B, on_floor, B, Has)).

solve(state(_, _, _, has)).

solve(State) :-
    move(State, Action, NewState),
    write(Action),
    nl,
    solve(NewState).