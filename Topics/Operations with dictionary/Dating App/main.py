def select_dates(potential_dates: list):
    people = []
    for person in potential_dates:
        if person["age"] > 30 and "art" in person["hobbies"] \
                and person["city"] == "Berlin":
            people.append(person["name"])
    return ", ".join(people)