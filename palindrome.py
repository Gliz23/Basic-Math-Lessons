name = "y r o r y"


letters_list = []

letters = name.split(' ')

for letter in letters:
    letters_list.append(letter)

new_list = []

for i in range(1,6):
    new_list.append(letters_list[-i])


if new_list == letters_list:
    print ("we have a palindrome")

else:
        print ("this is not a palindrome")