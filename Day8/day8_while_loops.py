# A while loop is used to perform an action as long as some condition is met

# To avoid an infinite loop, make sure that the value we're checking can be changed inside
# of the loop

# The break keyword allows us to break out of a loop, the continue keyword
# allows us to skip the rest of the code for the current iteration

# e.g.:
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

# EXERCISES

# 1) Write a short guessing game program using a while loop. The user should be prompted
# to guess a number between 1 and 100, and you should tell them whether their guess
# was too high or too low after each guess. The loop should keeping running until the user
# guesses the number correctly.

target_number = 22

# guess = int(input('Pick a number between 1 - 100: '))

# while int(guess) != target_number:
#     if guess < 1 or guess > 100:
#         guess = int(input('Sorry, that is an invalid number. Try again: '))
#     elif guess < target_number:
#         guess = int(input('Too low. Try again: '))
#     elif guess > target_number:
#         guess = int(input('Too high. Try again: '))
#     print('You guessed correct!')

# 2) Use a loop and the continue keyword to print out every character in the
# string "Python", except the "o".
for letter in 'python':
    if letter == 'o':
        continue
    print(letter)


# Remember that strings are collections, and they are iterable, so you can iterate over the string,
# which will yield one character at a time.

# 3) Using one of the examples from earlier—or a solution entirely of your
# own—create a program that prints out every prime number between 1 and 100.
primes = []

for nums in range(2, 101):
    for num in range(2, nums):
        if nums % num == 0:
            break
    else:
        primes.append(nums)


print(primes)
