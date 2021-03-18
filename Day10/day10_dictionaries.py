# Dictionaries
# A dictionary is an associative array (key, value pairs). They can't have a key
# without a value and values can't exist without a key

# Dictionaries are defined by curly braces

# e.g.:
student = {'name': 'John Smith'}

student_grades = {
    'name': 'Colin Deke',
    'grades': [88, 77, 93, 89]
}

# We retrieve values in a dictionary by accessing their keys
# e.g.:
print(student_grades['grades'])
# >>> [88, 77, 93, 89]
print(student_grades['grades'][1])
# >>> 77


# To check if a key exists, use the get method:
print(student_grades.get('grades'))

# if the value exists, grades will be printed, else the default result is none. Can specify
# for specific result if none:

print(student.get('grades', []))
# >>> []


# Adding items to a dictionary:
student = {
    'name': 'John Smith',
    'grades': [88, 76, 92, 85, 69]
}

student['age'] = 22

print(student)
# >>> {
#   'name': 'John Smith',
#   'grades': [88, 76, 92, 85, 69],
#   'age': 22
# }

# Extending a dictionary using the update method:
movie = {
    'title': 'Avengers: Endgame',
    'directors': ['Anthony Russo', 'Joe Russo'],
    'year': 2019
}

meta_info = {
    'runtime': 181,
    'budget': '$356 million',
    'earnings': '$2.798 billion',
    'producer': 'Kevin Feige'
}

movie.update(meta_info)

print(movie)

# >>>
# {
# 	'title': 'Avengers: Endgame',
# 	'directors': ['Anthony Russo', 'Joe Russo'],
# 	'year': 2019,
# 	'runtime': 181,
# 	'budget': '$356 million',
# 	'earnings': '$2.798 billion',
# 	'producer': 'Kevin Feige'
# }

# or:

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

movie.update({
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
})


# Deleting items from a dictionary

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019,
    "runtime": 181
}

del movie["runtime"]

# or pop:

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019,
    "runtime": 181
}

movie.pop('year')


# When iterating over dictionaries, by default, we only get keys:

for item in movie:
    print(item)

# >>>
# title
# directors
# runtime

# to get values, use the value method:
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

for value in movie.values():
    print(value)
# >>>
# Avengers: Endgame
# ['Anthony Russo', 'Joe Russo']
# 2019


# To get both the keys and values, use the items method:

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

for key, value in movie.items():
    print(f'{key}: {value}')

# >>>
# title: Avengers: Endgame
# directors: ['Anthony Russo', 'Joe Russo']
# year: 2019

# *** Note, Modern Python dictionaries are ordered in the order the key/values were added


# EXERCISES

# 1) Below is a tuple describing an album:

#  (
#  	"The Dark Side of the Moon",
#  	"Pink Floyd",
#  	1973,
#  	(
#  		"Speak to Me",
#  		"Breathe",
#  		"On the Run",
#  		"Time",
#  		"The Great Gig in the Sky",
#  		"Money",
#  		"Us and Them",
#  		"Any Colour You Like",
#  		"Brain Damage",
#  		"Eclipse"
#  	)
#  )


# Inside the tuple we have the album name, the artist (in this case, the band),
# the year of release, and then another tuple containing the track list.

# Convert this outer tuple to a dictionary with four keys.
album = {
    'name': 'The Dark Side of the Moon',
    'band': 'Pink Floyd',
    'year': 1973,
    'track_list': (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
}

# 2) Iterate over the keys and values of the dictionary you create in exercise 1.
# For each key and value, you should print the name of the key,
# and then the value alongside it.

for key, value in album.items():
    print(f'{key}: {value}')

# 3) Delete the track list and year of release from the dictionary you created.
#  Once you've done this, add a new key to the dictionary to store the date of release.
# The date of release for The Dark Side of the Moon was March 1st, 1973.
del album['year']
del album['track_list']

album['date_of_release'] = 'March 1st, 1973'

for key, value in album.items():
    print(f'{key}: {value}')

# If you use a different album for the exercises, update the date accordingly.


# 4) Try to retrieve one of the values you deleted from the dictionary.
# This should give you a KeyError. Once you've tried this,
# repeat the step using the get method to prevent the exception being raised.
# print(album['year'])
print(album.get('year'))
# >>> None

# Add default value 'unknown'
print(album.get('year', 'unknown'))
# >>> unknown
print(album.get('name', 'unknown'))
# >>> The Dark Side of the Moon
