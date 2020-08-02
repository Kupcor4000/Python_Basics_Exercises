import calendar
from datetime import date
#Exercise 11
print(abs.__doc__)
print()

print("_____________")

#Exercise 12
y = int(input("Please enter a year: "))
m = int(input("Please enter a month: "))
print(calendar.month(y,m))
print("")

print("_____________")

#Exercise 13
f_date = date(2020,7,2)
l_date = date(2020,7,20)
delta = l_date - f_date
print("Różnica dni: {}\n".format(delta.days))

print("_____________")

#Exercise 14
radius = int(6)
print("Volume of sphere: {}\n".format((4/3)*radius*radius*radius*3.14))

print("_____________")

#Exercise 15
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")