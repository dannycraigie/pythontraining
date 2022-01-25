#def add_calc(number1, number2):
#    answer = number1 + number2
#    return answer
#
#added_number = add_calc(5,5)
#print(added_number + 20)

# work out avg percentage grade of results
#def grade (name: str, homework: int, assess: int, exam: int):
#    sum1 = (homework * 4)
#    sum2 = (assess * 2)
#    scoravg = (sum1 + sum2 + exam) // 3
#    return name, scoravg
#print(grade("danny", 24, 45, 75))

# find max of 3 numebers
#def max_of_two( x, y ):
#    if x > y:
#        return x
#    return y
#def max_of_three( x, y, z ):
#    return max_of_two( x, max_of_two( y, z ) )
#print(max_of_three(3, 6, 8))

# multiply numbers in a list
#def multiply(numbers):  
#    total = 1
#    for x in numbers:
#        total *= x  
#    return total  
#print(multiply((8, 2, 3, -1, 7)))

#def reverse_text(x):
#    return x[::-1] 
#dctext = reverse_text("backwards")
#print(dctext)

def per_hundred(x):
    return(x/100)

answer = per_hundred(500)
print(answer)

