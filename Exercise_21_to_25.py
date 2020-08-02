#Ex 24 us_vowel
def is_vowel(char):
    all_vowel = 'aeiou'
    return char in all_vowel


#Exercise21 we are checking if the numbers which user enter to our program is even or odd
users_number = int(input("Please enter an integer number: "))
if users_number >= 0:
    if users_number % 2 == 0:
        print("Ta liczba jest jak najbardziej parzysta\n")
    else:
        print("Ta liczba nie jest parzysta\n")
else:
    print("Liczba musi byc wieksza od zera!\n")

print("________________________")

#Exercise 22
values = input("Type some numbers: ")
list = values.split()
print("List: ",list)
iterator = int(0)
for i in range(len(list)):
    print("{} : {}".format(i,list[i]))
    if int(list[i]) == int(4):
        iterator += 1
print("Liczba 4 powtórzyłą się {} razy w liscie {}\n".format(iterator,list))

print("________________________")


#Exercise 23
word = input("Please enter the word: ")
copies = int(input("How many copies do you want to do? "))
if len(word) < 2:
    print(copies*word)
else:
    print(copies*(word[0]+word[1]))
print()
print("________________________")

#Ex 24
a = input("Please enter a letter: ")
print("Is it a vowel? {}\n".format(is_vowel(a)))
print("________________________")

#Ex25
values = input("Type some numbers: ")
list = values.split()
print("List: ",list)
user_input = input("Please enter random number: ")
print("Czy liczba {} znajduje sie wewnatrz zbioru {}?".format(user_input,list))
print(user_input in list)
print("________________________")

