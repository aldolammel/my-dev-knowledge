travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["paris", "lille", "dijon"]
    },
    {
        "country": "germany",
        "visits": 5,
        "cities": ["berlin", "hamburg", "stuttgart"]
    },
]


# TODO: Write the function that will allow new countries to be added to the travel_log. 👇


def fnc_add_country(new_country, new_visits, new_cities):
    new_dict = dict()
    new_dict['country'] = new_country
    new_dict['visits'] = new_visits
    new_dict['cities'] = new_cities
    travel_log.append(new_dict)
    return None


fnc_add_country('czech republic', 4, ['prague', 'brno', 'celina'])  # country, times visited, [cities visited]
print(travel_log)
