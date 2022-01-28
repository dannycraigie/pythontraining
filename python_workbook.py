## 3    AREA OF A ROOM
#def room_volume():
#    roomlength = int(input("Please enter room length in metres "))
#    roomwidth = int(input("Please enter room width in metres "))
#    area = roomlength * roomwidth
#    return(f"Your room volume is {area} square metres")
#
#print(room_volume())

## 4    AREA OF A FIELD
#def fieldmeasure():
#    length = float(input("Enter field width in feet:"))
#    width = float(input("Enter field length in feet:"))
#    acreage = (length * width) / 43560
#    return(f"Your field measures {acreage:.2f} acres")
#
#print(fieldmeasure())

## 5    BOTTLE DEPOSITS
#def bottle_deposits():
#    cont = float(input("How many bottles 1 litre or less do you have?"))
#    cont2 = float(input("How many bottles over 1 litre do you have?"))
#    ans1 = cont *  0.10
#    ans2 = cont2 * 0.25
#    total = ans1 + ans2
#    return(f"You have returned {cont} small bottles at 10 cents and {cont2} large at 25 cents. Your deposit refund is ${total:.2f}")
#
#print(bottle_deposits())

## 6 TAX & TIPS
#def tax_and_tip():
#    meal = float(input("Please enter the cost of the meal: £"))
#    tip = (meal / 100) * 18
#    sub_total = tip + meal
#    tax = (sub_total / 100) * 20
#    total = sub_total + tax
#    return(f"""Meal Total = £{meal}\nTip @ 18% = £{tip:.2f}\nSub Total = £{sub_total:.2f}      
#Tax @ 20% = £{tax:.2f}\nGrand Total = £{total:.2f}""")  
#
#print(tax_and_tip())

######## 7 POSITIVE INTEGERS  ##### needed help with the maths
#def positive_integers():
#    n = int(input("Enter your positive integer "))
#    total = n * (n+1) / 2
#    return(f"""The total of all the positive integers up to {n} is {total:.0f}""")
#
#print(positive_integers())

## 8 WIDGETS AND GIZMOS
#def weight_of_items():
#    widget = int(input("Enter number of widgets "))
#    gizmo = int(input("Enter number of gizmos "))
#    widget_weight = widget * 75
#    gizmo_weight = gizmo * 112
#    weight = gizmo_weight + widget_weight
#    return (f"""Your widgets weigh {widget_weight} grams & your gizmos {gizmo_weight}.
#Giving a total weight of {weight} grams""")
#
#print(weight_of_items())

## 9 COMPOUND INTEREST
#def savings_account():
#    balance = float(input("Please enter your initial deposit amount £"))
#    interesty1 = (balance / 100) * 4
#    balyear1 = interesty1 + balance
#    interesty2 = (balyear1 / 100) * 4
#    balyear2 = balyear1 + interesty2
#    interesty3 = (balyear2 / 100) * 4
#    balyear3 = interesty3 + balyear2
#    return(f"""interest earned after 1 year is £{interesty1:.2f} with a closing balance of £{balyear1:.2f}
#compound interest for year 2 is £{interesty2:.2f} with a closing balance of £{balyear2:.2f}
#compound interest for year 3 is £{interesty3:.2f} with a closing balance of £{balyear3:.2f}""")
#
#print(savings_account())

## 10 Arithmetic
#from cmath import log10
#def calculator(a, b):
#    sum = a + b
#    diff = a - b
#    prod = a * b
#    quot = a / b    
#    rem = a % b
#    res = log10(a)
#    pow = a ** b 
#    return (f"""You entered {a} and {b}\nsum ={sum}\ndifference ={diff}\nproduct ={prod}
#quotient = {quot}\nremainder ={rem}\nlog10 ={res}\npower ={pow}""")
#
#print(calculator(2, 8))

## 11 FUEL EFFICIENCY
#def fuel_efficiency():
#    usa = int(input("What is your US MPG? "))
#    canada = 235.215 / usa
#    return (f"Your Canadian fuel efficiency equivalent is {canada:.2f} litres per 100km")
#
#print(fuel_efficiency())

## 12 DISTANCE BETWEEN TWO POINTS ON EARTH ######### Lots of help with the math but had the import
## and function formatted in my mind first. 2 of each input then convert with radians. Copied the 
## equation
#from math import radians, cos, sin, sqrt, pi, atan2
#def measure_earth():
#    lat1 = int(input("What is your 1st lattitude? "))
#    lat2 = int(input("and your 2nd? "))
#    lon1 = int(input("What is your 1st longitude? "))
#    lon2 = int(input("and your 2nd? "))
#    latd1 = radians(lat1)
#    latd2 = radians(lat2)
#    lond1 = radians(lon1)
#    lond2 = radians(lon2)
#    r = 6371.01
#    dlon = lond2 - lond1
#    dlat = lat2 - lat1
#    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)** 2
#    c = 2 * atan2(sqrt(a), sqrt(1 -a))
#    distance = r * c
#    return(f"The distance is {distance} km")
#
#print(measure_earth())




