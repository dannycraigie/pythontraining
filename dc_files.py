# opens file anc changes the text to upper
#openedfile = open("README.md")
#textstuff = openedfile.read()
#openedfile.close()
#print(textstuff)
#
#uppertext = textstuff.upper()
#
#print(uppertext)
#openedfile = open("READ.me", "w")
#openedfile.write(uppertext)
#openedfile.close()

#file = open("filename.txt", "r")

#outfile = ""

#for line in range(1, 10):
#    if line % 2 == 0:
#        outfile += file.readline()
#    else:
#        file.readline()

#file = open("filename.txt", "w")
#file.write(outfile)
#print(outfile)
#file.close()

#with open("teams.txt", "w") as file:
#    for n in range(1-6):
#        newline = "Team" + str(n) + "\n"
#        file.write(newline) 
        
file = open("teams.txt", "w")

for n in range(1,6):
    newline = "This is Team" + str(n) + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")

print(file.readlines(1))
file.readlines()
print(file.readlines(4))
file.readlines()

file.close()





