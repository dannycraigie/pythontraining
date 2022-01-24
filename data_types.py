var1 = "danny"
var1a = 'danny'
var2 = 50
var3 = True
var4 = 50.0
var5 = int(var2)
var6 = str(var2)

print("hello")
# sum
print(var2 + var2)

# escape \ escapes next character \t tab \U Extended Unicode
var6 = "Hello my name is \"Danny\""
print(var6)
print("Person 1: \tHey, how are you?\nPerson 2: \tGood thanks! \U0001F604")

# new lin \n
var7 = "I want text \n across two lines"
print(var7)

word1 = "Good"
word2 = "Day"
word3 = "John"

sentence = word1 + " " + word2 + " " + word3
print(sentence)

# f strings 
age = 46
print(f"Danny is {age} years old")
print(f"Danny will be {age + 10} years old in 10 years")