# Using join to convert lists to strings

project_authors = ['Mike', 'Sofia', 'Helen']
print(project_authors)

project_authors = ', '.join(project_authors)
print(project_authors)
print(f'The people who worked on this project are: {project_authors}.')


# If we want to join numbers we have to convert each number to a string first
numbers = [1, 2, 3, 4]

stringified_nums = []

for nums in numbers:
    stringified_nums.append(str(nums))

print(', '.join(stringified_nums))


# Split
user_numbers = '1, 2, 3, 4'
print(user_numbers)
print(user_numbers.split(','))
# >>> ['1', ' 2', ' 3', ' 4']

# split with list or tuple functions:
sample_string = 'Python'
print(list(sample_string))
print(tuple(sample_string))


# newline = \n
print('This is the best!\nYou da best!')
# >>> This is the best!
# >>> You da best!


# slicing:
og_string = 'Python'
sliced_string = og_string[0:3]
# or og_str[:3]
print(sliced_string)


# len function:
numbers = [12, 16, 22, 2, 5]
print(len(numbers))
# >>> 5


# Exercises
# 1) Ask the user to enter their given name and surname in response to a single prompt.
# Use split to extract the names, and then assign each name to a different variable.
# For this exercise, you can assume that the user has a single given name and a single surname.
# user_name = input('Please enter your first and last name: ')
# full_name = user_name.split(' ')
# first_name = full_name[0]
# last_name = full_name[1]
# print(first_name)
# print(last_name)

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
# Remember that you can only join collections of strings, so you’re going to need to do some
# initial processing of the list of numbers.
numbers = [1, 2, 3, 4, 5]
new_format = []

for num in numbers:
    new_format.append(str(num))

print(('|').join(new_format))

# 3) Below you’ll find a short list of quotes:

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(quote)
# Each quote is a string, but each string actually contains quote characters at the start and end.
# Using slicing, extract the text from each string, without these extra quote marks,
# and print each quote.
for quote in quotes:
    print(quote[1:-1])

# You may also want to try a solution using strip.
for quote in quotes:
    print(quote.strip("''"))

# 4) Ask the user to enter a word, and then print out the length of the word.
# You should account for any excess whitespace in the user’s input, so you’re going to
# have to process the string before you find its length.

# If you want to take this a little bit further, you an ask the user for a long piece of text.
# You can then tell them how many how many characters are in the text overall,
# and you can also provide them a word count.

user_text = input('Please enter a line of text: ')
words = len(user_text.split(' '))
chars = len(('').join(user_text.split(' ')))
print(words)
print(f'Your text contains {chars} characters and {words} words')
