def vacuum_cleaner():
    rooms = {
        "A": "Dirty",
        "B": "Dirty"
    }

    position = "A"

    print("Initial State:", rooms)

    for room in ["A", "B"]:
        position = room

        if rooms[position] == "Dirty":
            print("Cleaning room", position)
            rooms[position] = "Clean"

    print("Final State:", rooms)


vacuum_cleaner()
