from sys import argv #python test2.py filename
script, filename = argv

print("Hello World!")
#THIS IS A COMMENT
print("I will now count my chickens:")

print ("Hens", 25 + 30 / 6) #30
print ("Roosters", 100 - 25 * 3 % 4) #97
print ("Is it greater?", 5 > -2)
#FORMAT 
things=100;
things2=50;
print("%s things but I only have %d"% (things,things-things2))
domo="domo"*2

formatter = "%r %r \n%r %r"
print (formatter % (domo,domo,domo,domo))
#name=input("What is your name: ") #raw_input does onlys str inputs for security reasons

#READING AND WRITTING
txt = open(filename)
print (txt.read())
txt.close()
txt2 =open("test2_1.txt",'w')
txt2.truncate() #deletes all the data in the file
txt2.write("That pepsi sure is ice")
txt2.close()

the_count = [1, 2, 3, 4, 5]
for number in the_count:
    print ("This is count %d" % number)

num='25'
for x in range(0,2): #range(2) also works
    if '5' in num:
        print(num)
#Dictionary
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
# this fucntion takes no arguments
def print_none():
    print ("I got nothin'.")


