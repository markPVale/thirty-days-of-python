# Style note ***

# It's common convention to name a loop variable '_' when the number being generated
# is not in the code of the loop body
# e.g.:
# for _ in range(10):
# print('Hola')

# Exercises

# 1) Below we've provided a list of tuples, where each tuple contains details about an
# employee of a shop: their name, the number of hours worked last week, and their hourly rate.
# Print how much each employee is due to be paid at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    print(f'{employee[0]} has to be paid: {employee[1] * employee[2]}')


# 2) For the employees above, print out those who are earning an hourly wage above average.

# Hint: you can use a for loop and two variables to keep track of the total wage and the
# number of employees. Then, use the two variables to calculate the average.
# Finally, add another loop that goes through the employees list again and prints
# out only those who have an hourly wage above the calculated average.

total_wages = 0


for employee in employees:
    total_wages += employee[2]


average_wage = total_wages / len(employees)
print('ave wage = ', round(average_wage, 2))

for employee in employees:
    if employee[2] > average_wage:
        print((employee[0], employee[2]))
