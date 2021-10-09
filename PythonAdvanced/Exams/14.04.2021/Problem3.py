def flights(*args):
    dictionary = dict()
    cities = list()
    pasengers = list()

    for arg in args:
        if arg == 'Finish':
            break
        if isinstance(arg, str):
            cities.append(arg)
        elif isinstance(arg, int):
            pasengers.append(arg)

    for i in range(0, len(cities)):
        current_city = cities[i]
        current_passengers_count = pasengers[i]

        if current_city in dictionary:
            dictionary[current_city] += current_passengers_count
        else:
            dictionary[current_city] = current_passengers_count

    return dictionary


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
