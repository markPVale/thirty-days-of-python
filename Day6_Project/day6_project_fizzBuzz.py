# The brief
# For our version, we're only going to have a single player, the computer,
# and it's going to play the first 100 rounds of Fizz Buzz all by itself.
# In other words, we need to print out the first 100 items in the sequence,
# starting from 1.


for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 == 0:
        print('FizzBuzz')
    elif nums % 3 == 0:
        print('Fizz')
    elif nums % 5 == 0:
        print('Buzz')
    else:
        print(nums)
