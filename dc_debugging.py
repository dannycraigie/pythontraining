




#def is_prime(x):
#    if x < 2:
#        return False
#    for n in range(2, x-1):
#        if x % n == 0:
#            return False
#    else:
#        return True

#print(is_prime(2))
#print(is_prime(3))
#print(is_prime(4))
#print(is_prime(5))
#print(is_prime(6))
#print(is_prime(7))
#print(is_prime(15))
#print(is_prime(20))
#print(is_prime(25))

#import pdb
#pdb.set_trace()


#item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
#n = 0

#while n <5:
#    for i in item_list:
#        print(i)
#    n += 1

#print (item_list[n-1])


#def product(n):
#    total = 1
#    for n in n:
#        total *= n
#    return total

#print(product([4,4,5]))

user_funds = 10.31
item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price < user_funds:
    print("Sorry you don't have enough money")
