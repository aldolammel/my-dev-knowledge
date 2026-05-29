"""

DICTIONARY NESTING:

"""

# Dictionary nesting:
_capitals = {
    'Brazil': 'Brasilia',
    'Germany': 'Berlin'
}

# Nesting a List in a Dictionary:
_travelLog = {
    'Brazil': ['Porto Alegre', 'Fortaleza', 'Rio'],
    'Germany': ['Berlin', 'Munich']
}

# Nesting Dictionary in a Dictionary:
_travelLogBigger = {
    'Brazil':
        {
            'cities_visited': ['Porto Alegre', 'Fortaleza', 'Rio'],
            'total_visits': 12
        },
    'Germany':
        {
            'cities_visited': ['Berlin', 'Munich'],
            'total_visits': 3
        }
}

# Nesting Dictionary in a List:
_listWithDict = [
    {
        'country': 'Brazil',
        'cities_visited': ['Porto Alegre', 'Fortaleza', 'Rio'],
        'total_visits': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Munich'],
        'total_visits': 3
    }
]
