# Formatting Strings and Processing User Input

# String concatenation - joining two or more strings together

# hourly_wage = input('please enter your hourly wage: ')
# hours_worked = input('how many hours did you work this week: ')

# print('hourly wage: ' + hourly_wage)
# print('hours worked: ' + hours_worked)


# converting integers to strs:
age = str(28)
print(age)
print('yo man you know where number ' + age + ' is?')


# converting strings to integers:
age = int('28')


# converting strings to floats:
weight = float('29.3')


# TRUNCATION - the act of shortening something by removing some part of it.

# converting a float to an integer is going to truncate (cut it short) the float
car_weight = int(2285.67)
print(car_weight)

# =====================================================

# String Interpolation using the format method
# STRING INTERPOLATION - is the act of inserting some new content into an existing string

# format method:

format_string = '{} is {} years old!'.format('John', 24)
print(format_string)

new_format_string = '{0} is {1} years old, and {0} works as a {2}'
print(new_format_string.format('Mikey', 41, 'web developer'))

# the format method using variables:
output = '{name} is {age} years old, and {name} works as a {job}'
print(output.format(name='Johnny', age=24, job='web developer'))


# f-string method:

name = 'Chris'
age = 50

eff_string = f'{name} is {age * 2} years old!'

print(eff_string)


# =====================================================

# Basic String Processing

'Hola Mundo'.lower()
'Hola Mundo'.upper()
'Hola Mundo'.capitalize()
'Hola Mundo'.title()

# removing white space:
'   Hola Mundo  '.strip()


# =====================================================

# Exercises
# 1. Using the variable below, print "Hello, world!".

greeting = "Hello, world"

print(f'{greeting}!')
print('{}!'.format(greeting))
print(greeting + '!')

# 2. Ask the user for their name, and then greet the user, using their name
# as part of the greeting. The name should be in title case, and shouldn't be
# surrounded by any excess white space.

user_greeting = input('Hi, what is your name? ').strip().title()
# print(user_greeting)
print(f'Hello {user_greeting}')

# 3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".

# Remember that we can only concatenate strings to other strings, so you will have to
# convert the integer to a string before you can perform the concatenation.

age = 29
print(f'I am {str(age)}')


# 4. Format and print the information below using string interpolation:

title = "Joker"
director = "Todd Phillips"
release_year = 2019
# The output should look like this:

# Joker (2019), directed by Todd Phillips

print(f'{title} ({release_year}), directed by {director}')
