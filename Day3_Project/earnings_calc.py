#  A Simple Earnings Calculator

# 1) three prompts
# name
# hourly wage
# hours worked per week

# 2) name stripped of whitespace
# name title cased

# 3) total earnings / week = hours worked * hourly wage

# 4) keep in mind str conversion

# 5) output should be a single str:
# e.g. - Regina George earned $800 this week.


emp_name = input('Please enter your first and last name: ')
emp_name = emp_name.strip().title()
# print(emp_name)

hourly_wage = input('Please enter your hourly wage: ')
hourly_wage = float(hourly_wage)
# print(hourly_wage)

hours_worked = input('Please enter how many hours you worked this week: ')
hours_worked = float(hours_worked)
# print(hours_worked)

weekly_earnings = round((hourly_wage * hours_worked), 2)
# print(weekly_earnings)

print(f'{emp_name} earned ${weekly_earnings} this week')
