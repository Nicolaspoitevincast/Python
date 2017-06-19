#--------------------------------
# Programming Assignment 3
#
# Name: Nicolas Poitevin
# Date: 10/29/2014
#
#--------------------------------
#################################
# Exercise P4.3 (8 points)
#string= input("Please enter a string: ")
#for s in string: #ONLY THE UPPERCASE
#    if s.isupper():
#        print(s, end="")
#print("")
#for i in range(0,len(string),2): #EVER SECOND LETTER
#    print(string[i], end="")
#print()
#for s in string: #REPLACES VOWELS WITH UNDERSCORE
#    if s.lower() in "oeiuay":
#        print("_",end="")
#    else:
#        print(s,end="")
#print()
#digitNum=0 #COUNTS NUMBER OF DIGITS IN STRING
#for s in string:
#    if s.lower().isdigit():
#        digitNum+=1
#print("There is ",digitNum," digit in your string!")
#num=[] #Prints indices of vowels
#for i in range(0,len(string)):
#    if string[i] in "oeiuay":
#        num+=[i]
#print(num)
#################################
# Exercise P4.7 (8 points)
#from random import randint
#word= input("Please input a word: ")
#word2=""
#rang= len(word)-1
#for w in range(0,len(word)):
#    i = randint(0,rang-1)
#    j = randint(i+1,rang)
#    if j != rang:
#        word2= word[0:i]+word[j]+word[(i+1):j]+word[i]+word[(j+1):]
#    else:
#        word2= word[0:i]+word[j]+word[i+1:j]+word[i]
#    print(word2)
#################################
# Exercise P4.14 (8 points)
#Read the Notes section posted online with this assignment
#Save the collected values in a list 
#and use the first (and more accurate) standard deviation formula
#another = True
#values=[float(input("Please enter a number: "))]
#while another:
#    value=input("Please enter more numbers or a letter if you are finished :")
#    if value.isalpha():
#        another = False
#    else:
#        values+=[float(value)]
#n=0
#average=0
#summation =0
#for i in values:
#    n+=1
#    average+=i
#average= average/n
#for i in values:
#    summation+= (i-average)**2
#s = (summation/(n-1))**(.5)
#print(s)
#################################
# Exercise P4.15 (8 points)
#f1=1
#f2=1
#f=0
#n = int(input("Please enter a value for n in the nth term of the fibonacci sequence: "))
#for i in range(3,n):
#    f=f1+f2
#    f1=f2
#    f2=f
#print(f)
#################################
# Exercise P4.23  (10 points)
#from random import randint
#marbles = randint(10,100)
#turn= randint(0,1)
#takes=0
#test=False
#n=6
#mode = int(input("0 for stupid mode and 1 for smart mode: "))
#print("There are ",marbles," marbles in the bag")
#while marbles > 1:
#    if turn ==0:
#        print("Comp's Turn:")
#        if mode==0:
#            takes=randint(1,int(marbles/2))
#        elif mode ==1:
#            while test == False:
#                x=int(marbles/2)
#                while test == False and x > 0:
#                    if int((2**n)-1) == x:
#                        takes=x
#                        test =True
#                    else:
#                        x=x-1
#                n= n-1
#            n=6
#            test=False
#        marbles = marbles-takes
#        if marbles ==1:
#            print("THE COMP WON")
#        else:
#            print("The comp took ",takes," marbles so ",marbles," are left")
#        print("Your Turn:")
#        takes = int(input("Please input how many marbles you wish to take:" ))
#        while takes < 1 or takes > int(marbles/2):
#            takes = int("Please enter a valid input: ")
#        marbles = marbles-takes
#        if marbles == 1:
#            print("WINNER")
#        else:
#            print("There are ",marbles," left in the bag")
#    elif turn==1:
#        print("Your Turn:")
#        takes = int(input("Please input how many marbles you wish to take: "))
#        while takes < 1 or takes > int(marbles/2):
#            takes = int("Please enter a valid input: ")
#        marbles = marbles-takes
#        if marbles == 1:
#            print("WINNER")
#        else:
#            print("There are ",marbles," left in the bag")
#        print("Comp's Turn:")
#        if mode==0:
#            takes=randint(1,int(marbles/2))
#        elif mode ==1:
#            while test == False:
#                x=int(marbles/2)
#                while test == False and x > 0:
#                    if int((2**n)-1) == x:
#                        takes=x
#                        test =True
#                    else:
#                        x=x-1
#                n= n-1
#            n=6
#            test=False
#        marbles = marbles-takes
#        if marbles ==1:
#            print("THE COMP WON")
#        else:
#            print("The comp took ",takes," marbles so ",marbles," are left")    
#################################
# Exercise P4.25 (10 points)
#from random import randint
#s1=0
#s2=0
#goat=False
#for x in range(0,1000):
#    car = randint(1,3)
#    player= randint(1,3)
#    while not goat:
#        goat1=randint(1,3)
#        if goat1 != car and goat1 != player:
#            goat=True
#    goat = False
#    if player != car:
#        s1+=1
#    else:
#        s2+=1
#print("Counter for strategy 1: ",s1)
#print("Counter for strategy 2:",s2)
#################################
# Exercise P4.26 (8 points)
#a=32310901
#b=1729
#m=2**24
#rOld = int(input("Please enter a seed: "))
#for x in range(0,100):
#    rNew= (a*rOld+b)%m
#    rOld=rNew
#    print(rNew)
#################################
# Exercise Business P4.31 (8 points)
#tickets=100
#buyers=0
#while tickets > 0:
#    sold= int(input("Please enter how many tickets you wish to purchase: "))
#    while sold > 4 or sold < 1:
#        sold = int(input("The maximum amount of tickets that can be sold is 4: "))
#    buyers +=1
#    tickets= tickets-sold
#    print("The amount of tickets left are ",tickets)
#print(buyers)
#################################
# Exercise Business P4.33 (8 points)
#n = input("Please enter an 8-digit number: ")
#y1=0
#y2=0
#m=""
#for x in range(len(n)-1,-1,-2):
#    y1+=int(n[x])
#for x in range(0,len(n),2):
#    m+=str(int(n[x])*2)
#for x in m:
#    y2+=int(x)
#y3= y1+y2
#if (y3%10) == 0:
#   print("The number is valid")
#else:
#    check= int(n[len(n)-1])
#    y3=y3-check
#    for x in range(1,10):
#        if (y3+x)%10 ==0:
#               check=x    
#    print("Sorry your number isn't valid")
#    print("If you check digit was ",check," your number would be valid")
#################################
# Exercise Science P4.34 (8 points)
#a=float(input("Please input the rate at which prey birth exceeds natural death: "))
#b=float(input("Please input the rate of predation: "))
#c=float(input("Please input the rate at which predator deaths exceed births without food: "))
#d=float(input("Please input the rate of predator increase in the presence of food: "))
#iPrey=int(input("Please input the intial prey population size: "))
#iPred=int(input("Please input the intial predator population size: "))
#peroids =int(input("Please input the amout of peroids desired: "))
#prey=0
#pred=0
#index=0
#while peroids > index:
#    prey=iPrey*(1+a-b*iPred)
#    pred= iPred*(1-c+d*iPrey)
#    iPrey=prey
#    iPred=pred
#    index+=1
#print("The population size of predators are",int(pred))
#print("The population size of prey are",int(prey))
#################################
# Exercise Science P4.37 (8 points)
# Read the Notes section posted online with this assignment
#from math import e
#from math import log10
#t=0
#h=6
#x=1
#while t < 24:
#    t+=1
#    x = 1/(e**(t*(log10(2)/h)))
#    print("The relative amount left after ",t," hours is ",x)
#################################
# Exercise Science P4.38 (8 points)
#r0=20
#rS=8
#v=40
#n=.01
#pMax = 0
#p=0
#nMax=0
#while n <= 2:
#    p=rS*((n*v)/(n*n*r0+rS))**2
#    if p > pMax:
#        pMax=p
#        nMax=n
#    n+=.01
#print("Where the maximum power is outputed the turn ratio is %.2f"%nMax)

