var1 = input("Please type in a number: ")
var2 = input("Please type in another number: ")
var3 = input("Please type in yet another number: ")

# == is equal to, != not equal to, < less than, > greater than,
# <+ less or equal, >= greater than or equal to
#               and  both sides must be true
#                or  either side is true
#               or not
#               and not
if var1 >= var2 and var1 != var3:
    print("My boolean is outputting true")
else:
    print("My boolean is outputting false")



treevar1 = input("Type in a tree: ")
trees = ["larch", "oak", "pine", "willow"]

if treevar1 in trees:
    print("You have typed a tree from the list")
else:
    print("Fail") 


numvar1 = int(input("Type in a number"))
if numvar1 < 10:
    print("Your number is a single digit number")
elif numvar1 < 100:
    print("your number is a 2 digit integer")
elif numvar1 < 1000:
    print("You have a 3 digit integer")
elif numvar1 < 10000:
    print("You have a 4 digit integer")