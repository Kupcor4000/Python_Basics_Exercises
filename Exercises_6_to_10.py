
#Exercise 6
values = input("Type some numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List: ",list)
print("Tuple: ",tuple,"\n")

print("__________________")

#Exercise 7 - wypisywanie rozszerzenia pliku
filename = input("Input filename: ")
extension = filename.split(".")
print("Extension of this file is: {}\n".format(repr(extension[-1])))

print("__________________")

#Exercise 8
color_list = ["Red","Green","White","Black"]
print("First color: ",color_list[0])
print("Last color: ",color_list[3],"\n")

print("__________________")

#Exercise 9
exam_st_date = (11,12,2014)
print("The examination will be at: %i %i %i"%exam_st_date) #działa to podobnie jak w C
print("")

print("__________________")

#Exercise 10
n = input("Please enter your number: ")
a = int(n)
b = int(n+n)    #łączymy stringi a następnie zamieniamy je na integer
c = int(n+n+n)
print(b)
print(c)
print("n+nn+nnn = {}".format(a+b+c))