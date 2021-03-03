from itertools import zip_longest

# Unpacking - generally is used to perform several assignments at once by extracting
# individual values from some iterable. (aka - 'destructuring')

# e.g.-
movie = ('12 Angry Men', 'Sidney Lumet', 1957)

title = movie[0]
director = movie[1]
year = movie[2]

# or, to be more concise:
title, director, year = movie

# Python sees that we have three values and three variables and assigns them in order

# unpacking in a for loop:

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    title, director, year = movie
    print(f'{title}, {year} directed by {director}')


# Ignoring values:
for title, _, year in movies:
    print(f'The movie {title}, made in {year} was ...')


# Using * to collect values:
head, *tail = [1, 2, 3, 4, 5]
print(head)
# >>> 1
print(tail)
# >>> [2, 3, 4, 5]

first, second, third, *rest = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(rest)
# >>> ['d', 'e', 'f', 'g']

# Enumeration
# returns results in a numbered fashion by gererating a counter alongside the
# values in an iterable.

names = ['Eric', 'Austin', 'Ryan']

for counter, name in enumerate(names, start=1):
    print(f'{counter}. {name}')

for counter, (title, director, year) in enumerate(movies, start=1):
    print(f'{counter}. {title} ({year}), by {director}')

# >>>
# 1. Eternal Sunshine of the Spotless Mind (2004), by Michel Gondry
# 2. Memento (2000), by Christopher Nolan
# 3. Requiem for a Dream (2000), by Darren Aronofsky


# Zip
# Combines two or more iterables into a single iterable

# e.g.:
pet_owners = ['Paul', 'Cadie', 'Fredo']
pets = ['Bam', 'Bubbles', 'Pickles']

pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))
# >>>
# [('Paul', 'Bam'), ('Cadie', 'Bubbles'), ('Fredo', 'Pickles')]

# Using zip in for loops:
for owner, pet in zip(pet_owners, pets):
    print(f'{owner} owns {pet}')
# >>>
# Paul owns Bam
# Cadie owns Bubbles
# Fredo owns Pickles


# Breaking up a zip object:
zipped = [('John', 26), ('Anne', 31), ('Peter', 29)]
names, ages = zip(*zipped)

print(names)
# >>> ('John', 'Anne', 'Peter')
print(ages)
# >>> (26, 31, 29)


# ***CAVEAT FOR USING ENUMERATE AND ZIP***
# enumerate and zip are consumed when we iterate over them, they produce an 'iterator'
# To bypass this side effect, convert the iterator to a list or tuple


# Exercises

# 1) Below is some simple data about characters from BoJack Horseman:

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# The data contains the character name, the voice actor or actress who plays them,
# and the species of the character.

# Write a for loop that uses destructuring so that you can print each tuple in the following
# format:

# BoJack Horseman is a horse voiced by Will Arnet.

# Note that you're going to have to change the species information to
# lowercase when you print it. If you need a reminder on how to do this, we covered
# it in day 3 of the first week.

for characters in main_characters:
    character, actor, species = characters
    print(f'{character}, is a {species.lower()} voiced by {actor}')


# more concise:
for character, actor, species in main_characters:
    print(f'{character}, is a {species.lower()} voiced by {actor}')

# 2 2) Unpack the following tuple into 4 variables:

# ("John Smith", 11743, ("Computer Science", "Mathematics"))

# The data represents a student's name, their student id number, and their major
# and minor disciplines in that order.

name, id, (major, minor) = ("John Smith", 11743,
                            ("Computer Science", "Mathematics"))
print(f'The students name: {name}, id: {id}, major: {major}, minor: {minor}')


# 3) Investigate what happens when you try to zip two iterables of different lengths.
# For example, try to zip a list containing three items, and a tuples containing four items.

cars = ['Laborghini', 'Porsche', 'Ford']
drivers = ('Mario', 'Andrea', 'Shay', 'Axel')
cars_and_drivers = list(zip(cars, drivers))
print(cars_and_drivers)
# The element that exceeds the population of the other is left off, only those paired
# are included in the function.

# zip_longest will zip the longest tuple and fill in the missing values
# import zip_longest from the itertools module

longest_cars_and_drivers = list(zip_longest(cars, drivers, fillvalue='_'))
print(longest_cars_and_drivers)
# >>> [('Laborghini', 'Mario'), ('Porsche', 'Andrea'), ('Ford', 'Shay'), ('_', 'Axel')]
