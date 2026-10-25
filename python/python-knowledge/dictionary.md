#### Python > Containers > Dictionary
# Dictionary examples

---

### Nesting
```python
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
```

### Checking boolean values nested in one list per key
```python
all_options = {
	"A": [
		True,
		True,
	],
	"B": [	
		True,
		False,
	],
}

# If all options are False, regardless if from "A" or "B", tell me:
if not any(
	option
	for options in all_options.values()
	for option in options
):
	print("At lease one option should be True.")
	# Output: you wouldn't see this message!

# If any "B" option is True, tell me:
if any(all_options["B"]):
	print("For non-crew's seat, you cannot check any military skill.")
	# Output: you would see this message!
```

### xxxxxxxxxxxxxxxxxxx
```python
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

fnc_add_country('czech republic', 4, ['prague', 'brno', 'celina']) # country, times visited, [cities visited]
print(travel_log)
```

### Converting from and to other container formats
[/python/python-knowledge/dictionary-converting.py](/python/python-knowledge/dictionary-converting.py)
### ==Work to do here, aldo: to bring examples from here (link) and organize'em here (this file)==
[/python/python-knowledge/dictionary.py](/python/python-knowledge/dictionary.py)


