# Conditionals and Booleans

# In Python True & False

# Python falsy values:
# -Any numeric representation of 0
# -The values False an None
# -Empty sequences and other collections


# is and is not
# is and is not don't compare values but rather the same 'item'
# e.g.- The == operator is checking to see that two containers contain the exact same items, while
# is checks that we're talking about the same container (stored in the same memory address)

# id function:
# returns the memory address of an item, we can then verify if they are the same

a = ['a', 'b', 'c']
b = ['a', 'b', 'c']

print(id(a))
# >>> 140688866201472
print(id(b))
# >>> 140688876532928
print(a is b)
# >>> False

b = a
print(id(a))
# >>> 140645481369472
print(id(b))
# >>> 140645481369472

print(a is b)
# >>> True


# Order of Operations
#  Comparison operators are always lower priority than arithmetic operators


# Conditional Statements
# if
#  Conditional statements allow us to run some block of code if and only if the condition is met


# Exercises

# 1) Try to approximate the behaviour of the is operator using ==.
# Remember we have the id function for finding the memory address for a given value,
# and we can compare memory addresses to check for identity.

a = [1, 2, 3]
b = [1, 2, 3]

print('**', a == b)
# >>> True
print(a is b)
# >>> False
print(id(a) == id(b))
#  >>> False


# 2) Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(numbers)
print(id(numbers))
# >>> 140523838164864
print(numbers + [5] is new_numbers)
# >>> False
print(new_numbers)
# >>> [1, 2, 3, 4, 5]
print(numbers)
# >>> [1, 2, 3, 4]
print(id(new_numbers))
# >>> 140523856941248
print(numbers is new_numbers)
# >>> False

# And this:

numbers1 = [1, 2, 3, 4]

print(numbers1)
print(id(numbers1))


numbers1.append(5)


print(numbers1)
print(id(numbers1))

print(numbers1 is numbers1.append(5))
# >>> False

# new_numbers and numbers are not the same thing
# numbers1 and numbers1.append(5) are the same thing


# 3) Ask the user to enter a number.
# Tell the user whether the number is positive, negative, or zero.

user_input = int(input('Enter a number: '))

if user_input == 0:
    print('you chose 0')
elif user_input > 0:
    print('you chose a positive number')
else:
    print('you chose a negative number')


# 4) Write a program to determine whether an employee is owed any overtime.
# You should ask the user how many hours the employee worked this week,
# as well as the hourly wage for this employee.

employee = input("Please enter employee name: ")
hours_worked = input("Please enter the hours worked: ")
wage = input("Please enter the employee's wage: ")
ot = float(hours_worked) - 40

if ot > 0:
    print(f'{employee.title()} is due some additional pay in the amount of ${(ot * float(wage)) * 1.1}')
else:
    print(f'{employee.title()} is owed: ${float(hours_worked) * float(wage):.2f}')
