travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 25
    }
]


def add_new_country(country, visits, cities):
    new_country = {}
    new_country['country'] = country
    new_country['cities_visited'] = cities
    new_country['total_visits'] = visits
    travel_log.append(new_country)
    

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)