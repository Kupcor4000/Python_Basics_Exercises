import sys
import datetime

#Exercise 1
print("Twinkle, twinkle, little star,")
print("         How I wonder what you are! ")
print("                 Up above the world so high,")
print("                 Like a diamond in the sky. ")
print("Twinkle, twinkle, little star,")
print("         How I wonder what you are\n")

print("__________________")

#Exercise 2
print("Python Version")
print(sys.version)
print("Version info")
print(sys.version_info,"\n")

print("__________________")

#Exercise 3
print("Aktualna data: ")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print()

print("__________________")

#Exercise 4
radius = float(input("Please enter the value of the radius: "))
print("Area of the circle is equal: {}\n".format(3.14*radius*radius))

print("__________________")

#Exercise 5
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
print("Hello Mr. {} {}\n".format(surname,name))
