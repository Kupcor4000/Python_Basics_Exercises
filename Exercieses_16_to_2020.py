def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str #czyli jednak można zrobić kilka returnów w funckji

def powtarzenie(str,n):
    result = ""
    for i in range(n):
        result = result + str
    return result

#Exercise 16
user_number = float(input("Please enter a number: "))
if user_number > 17:
    print("Result: {}\n".format(abs(2*(user_number-17))))
else:
    print("Result: {}\n".format(user_number-17))

print("__________")

#Exercise 17
user_number2 = float(input("Please enter a number: "))
if user_number2 <= 1000 and user_number2 >= 100:
    print("{} zawiera sie w przedziale <100,1000>".format(user_number2))
elif user_number2 == 2000:
    print("{} jest równe 2000".format(user_number2))
else:
    print("{} nie zawiera sie w przedzialach <100,1000> ani nie jest rowne 2000".format(user_number2))
print()

print("__________")

#Exercise 18
a = float(input("Please enter first number: "))
b = float(input("Please enter second number: "))
c = float(input("Please enter third number: "))
wynik = a+b+c
if a==b and a==c:
    print("Sum of three numbers is equeal: {} {} {}\n".format(wynik,wynik,wynik))
else:
    print("Sum of three numbers is equeal: {} \n".format(wynik))

print("__________")

#Exercise 19
print(new_string("Empty"))
print(new_string("IsEmpty\n"))

print("__________")

#Exerciese 20
print(powtarzenie('Piter',2))
print(powtarzenie('Kupczyk',10))