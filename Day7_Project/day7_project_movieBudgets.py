# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 20000000),
#     ("Memento", 9000000),
#     ("Requiem for a Dream", 4500000),
#     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#     ("Avengers: Age of Ultron", 365000000),
#     ("Avengers: Endgame", 356000000),
#     ("Incredibles 2", 200000000)
# ]

# # For this project, your program should do the following:

# # 1) Calculate the average budget of all movies in the data set.
# total_budgets = 0

# for movie in movies:
#     total_budgets += movie[1]

# ave_budget = total_budgets / len(movies)


# # 2) Print out every movie that has a budget higher than the average you calculated.
# # You should also print out how much higher than the average the movie's budget was.
# above_budget_movies = []
# movie_overages = ("picture", 0)

# for movie in movies:
#     if movie[1] > ave_budget:
#         movie_overages = (movie[0], (movie[1] - ave_budget))
#         above_budget_movies.append(movie_overages)

# # print(above_budget_movies)
# # >>> [('Pirates of the Caribbean: On Stranger Tides', 188500000.0),
# # ('Avengers: Age of Ultron', 174500000.0), ('Avengers: Endgame', 165500000.0),
# # ('Incredibles 2', 9500000.0)]

# # 3) Print out how many movies spent more than the average you calculated.
# total_above_budget = len(above_budget_movies)

# # 4) If you want a little extra challenge, allow users to add more movies to the
# # data set before running the calculations.
# print(movies)


# add_movie = input('Add a movie: ')
# add_budget = input('What is the overall budget of the movie you added? ')
# additional_movies = (add_movie, add_budget)
# movies.append(additional_movies)
# print(movies)
# print(above_budget_movies)
# print(total_above_budget)


movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

add = input('How many movies would you like to add?')


for _ in range(int(add)):
    name = input('Enter a movie title: ')
    budget = input('Enter a movie budget')
    new_addition = (name, int(budget))
    movies.append(new_addition)


total_budgets = 0

for movie in movies:
    total_budgets += movie[1]

ave_budget = total_budgets / len(movies)

for movie in movies:
    if movie[1] > ave_budget:
        print(
            f'{movie[0]} cost {movie[1]:,}: {(movie[1] - ave_budget):,} over budget')
