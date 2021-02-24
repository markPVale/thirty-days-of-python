# Strings, Variables and Getting Input from Users

# Expressions represent something, like a number, a string, or an instance of a class.
# Any value is an expression!

# Anything that does something is a statement. Any assignment to a variable or function
# call is a statement. Any value contained in that statement in an expression.

# TRACEBACK - traceback
#   A traceback is a report that gives us information about what was happening
# in our code when an exception occured.

# name = input('please enter your name: ')

# print(name)


# Exercises
# Now that we’ve covered how to use strings, variables, and the input function, it’s time to practice with some exercises.

# 1) Ask the user for their name and age, assign theses values to two variables,
# and then print them.

userName = input('please enter your name: ')
userAge = input('please enter your age: ')

print(userName, userAge)

# 2) Investigate what happens when you try to assign a value to a variable that you’ve
# already defined. Try printing the variable before and after you reuse the name.

userName = 'kidCapri'
print(userName)
# >>> kidCapri
# the variable is defined to a new value

# 3) Below you’ll find some code with a number of errors. Try to go through the program
# line by line and fix the issues in the code. I’d encourage you to try running the program
# while you’re working on it, as reading the error messages is great practice for debugging
# your own programs.

# hourly_wage = input("Please enter your hourly wage: ')

# prnt("Hourly wage: ")
# print(hourlywage)
# print("Hours worked: ")
# print(hours_worked)

# hours_worked = input("How many hours did you work this week? ")

# >>> File "/Users/markvale/30DaysOfPython/Day2/d2.py", line 42
#     hourly_wage = input("Please enter your hourly wage: ')
#                                                           ^
# SyntaxError: EOL while scanning string literal


hourly_wage = input('Please enter your hourly wage: ')

print("Hourly wage: ")
print(hourly_wage)


hours_worked = input("How many hours did you work this week? ")
print("Hours worked: ")
print(hours_worked)
