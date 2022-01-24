devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters Smash tournament!")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")


mark =int(input("please enter a mark: "))
if mark > 85:
    print("Distinction")
elif mark > 65 and mark < 85:
    print("Pass")
else:
    print("fail")

# identify odd or even numbers
number = int(input("Please enter a number: "))
if (number% 2) == False:
    print("Nunber is even")
else:
    print("Number is odd")


# ientify vowels or consonants
letter = input("Please enter a letter: ")
vowel = ("a", "e", "i", "o", "u")
if letter in vowel:
    print("Your letter is a vowel")
elif letter != "y":
    print("Your letter is a consonant")
else:
    print("Y is sometimes a vowel and Y is sometimes a consonant")



number2 = int(input("Please enter number of sides to your shape: "))
if number2 == 3:
    print("Your shape is a triangle")
elif number2 == 4:
    print("your shape is a square")
elif number2 == 5: 
    print("your shape is a Pentagon")
elif number2 == 8:
    print("your shape is a hexagon")
else:
    print("I don't know that shape yet")

