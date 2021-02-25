# LISTS - lists are containers for other values.

# e.g.:
colors = ['red', 'blue', 'yellow']

movie_titles = [
    'John Wick',
    'Memento',
    'Requiem for a Dream'
]


# SUBSCRIPTION EXPRESSION - subscriptions experessions are used for accessing values
# in many collections and in sequences, for accessing elements by index.

# e.g.:
names = ['John', 'Alex', 'Jose']
print(names[1])


# Append:
names.append('Simon')
print(names)
# >>> ['John', 'Alex', 'Jose', 'Simon']

# ***Note*** append mutates the original list
#  If you want to avoid mutating the og list:

new_emp = ['Calvin']
updated_names = names + new_emp
print(updated_names)
# >>> ['John', 'Alex', 'Jose', 'Simon', 'Calvin']


# Insert
numbers = [1, 2, 3, 5]
numbers.insert(3, 4)
print(numbers)
# >>> [1, 2, 3, 4, 5]

# Remove

server_names = ["John", "Sarah", "Alice", "John"]
server_names.remove('John')
print(server_names)
# >>> ['Sarah', 'Alice', 'John']


# del
server_names = ["John", "Sarah", "Alice", "John"]
del server_names[1]
print(server_names)
# >>> ["John", "Alice", "John"]


# pop
#  In python, by default pop removes the last item on a list but an index can also be used to
# specify which item to remove

# Tuples
# Similar to lists
# wrapping w/ parenthesis is good practice
# if a tuple has a single item, it still needs a comma at the end

# Tuples are immutable
# You can only use + to join tuples
# This can be desirable since it ensures the integrity of the data structure
# e.g.:
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
# The list of tuples above w  ill always have tuples displaying: title, director, year
# and in that order


# Exercises:
# 1) Create a movies list containing a single tuple. The tuple should contain a movie title,
# the director’s name, the release year of the movie, and the movie’s budget.
movies = [('The Dark Knight', 'Christopher Nolan', 2008, '$185m')]

# 2) Use the input function to gather information about another movie.
# You need a title, director’s name, release year, and budget.
title = input('Enter a movie title: ').title()
director = input('Enter the director of the movie: ').title()
release_date = input("Enter the movie's release year: ")
budget = input("Enter the movie's budget: ")


# 3) Create a new tuple from the values you gathered using input.
# Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movie = (title, director, release_date, budget)
print(new_movie)

# 4) Use an f-string to print the movie name and release year by accessing your new movie tuple.
title_year = f'{new_movie[0]}, {new_movie[2]}'
print(title_year)

# 5) Add the new movie tuple to the movies collection using append.
movies.append(new_movie)
print(movies)

# 6) Print both movies in the movies collection.
print(movies[0][0], movies[1][0])

# 7) Remove the first movie from movies. Use any method you like.
del movies[0]
print(movies)
