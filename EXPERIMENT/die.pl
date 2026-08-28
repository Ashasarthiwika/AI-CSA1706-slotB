diet(diabetes, 'Eat vegetables, whole grains and avoid sugar').
diet(hypertension, 'Eat fruits, vegetables and reduce salt').
diet(obesity, 'Eat low calorie food and exercise regularly').
diet(anemia, 'Eat spinach, beans and iron rich food').

suggest_diet(Disease) :-
    diet(Disease, Diet),
    write('Recommended Diet: '),
    write(Diet),
    nl.