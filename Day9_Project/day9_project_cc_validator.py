# Using the Luhn Algorithm

# The way we're going to use the algorithm is as follows:

# 1) Remove the rightmost digit from the card number.
# This number is called the checking digit, and it will be excluded from most of our calculations.

# 2) Reverse the order of the remaining digits.

# 3) For this sequence of reversed digits, take the digits at each of the
# even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9,
# subtract 9 from those numbers.

# 4) Add together all of the results and add the checking digit.

# 5) If the result is divisible by 10, the number is a valid card number.
# If it's not, the card number is not valid.


# The brief
# The program you write for this project should do the following:

# 1) It should be able to accept a card number from the user.
# For this project, you can assume that the number will be entered as a
# single string of characters (i.e. there won't be any spaces between the numbers).
# However, you should be able to accept a card number with spaces at the start or
# end of the string.

cc_num = input('Please enter a valid credit card number: ').strip()
list_cc_num = list(cc_num)
int_list = []

for item in list_cc_num:
    int_list.append(int(item))

# If you want to challenge yourself, you should try to be more versatile
# with regards to the format that you accept card numbers in.

# You may want to turn the user's input into a list of numbers, as that will
# make it easier to work with.

# 2) The program should validate that card number using the Luhn algorithm
# described above. You should implement this algorithm yourself.

check_num = int_list[-1]
print('check number: ', check_num)

int_list.pop()

cc_rem_last_digit = int_list
rev_num = reversed(cc_rem_last_digit)
rev_list = list(rev_num)

dd_even = []

# for i in range(0, len(rev_list)):
#     if i % 2 == 0:
#         dd_even.append(rev_list[i] * 2)
#     else:
#         dd_even.append(rev_list[i])

for index, digit in enumerate(rev_list):
    if index % 2 == 0:
        dub_d = digit * 2

        if dub_d > 9:
            dub_d = dub_d - 9

        dd_even.append(dub_d)
    else:
        dd_even.append(digit)

# print('dd_even: ', dd_even)

# dd_sub_nine = []

# for i, digit in enumerate(dd_even):
#     if i % 2 == 0 and digit > 9:
#         dd_sub_nine.append(digit - 9)
#     else:
#         dd_sub_nine.append(digit)


# total_sum = 0

# for digit in dd_even:
#     total_sum += digit


total_check = sum(dd_even) + check_num
print(total_check)

# After removing the checking digit and reversing the card number, you'll
# need a for loop to go over the credit card numbers. As you go through each
# digit, you must find a way to determine whether a digit is in an odd or an
# even position. Remember you can check the model solution if you get stuck!

# 3) Once the validation is complete, the program should inform the user
# whether or not the card number is valid by printing a string to the console.
if total_check % 10 == 0:
    print(f'The card number you entered: {cc_num} is a valid card number.')
else:
    print(f'The card number you entered: {cc_num} is invalid.')
