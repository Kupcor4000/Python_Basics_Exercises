#Ex 26 creation of histogram
def histogram(items):
    for n in items:
        print(n*"+")

histogram([1,2,3,4,8,4,5,8,111])
#Brawo uprosciles program ze strony o 5 linijk
print("")
print("___________")

#Ex 27 concaenate elemnts in the list
values = input("Type something: ")
list = values.split()
print("List: ",list)
#Tworzymy jeden string z listy:
wyraz = ""
for i in range(len(list)):
    wyraz += list[i]
print("Polaczenie elemntow z listy daje nam: {}".format(wyraz))
print("")
print("______________")

#Ex 28 wypisanie liczb parzystych z listy
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for pa in range(len(numbers)):
    if numbers[pa] % 2 == 0:
        print(numbers[pa])
print("")
print("______________")

#Ex 29
color_list_1 = set(["white","Black","Red"])
color_list_2 = set(["Red","Green"])
print(color_list_1.difference(color_list_2))
print("")
print("______________")

#Ex 30 - area of triangle
base = float(input("Please enter the base of the triangle: "))
height = float(input("Please enter the height of the triangle: "))
print("Area of triangle is equal: {}\n".format((1/2)*height*base))
print("______________")