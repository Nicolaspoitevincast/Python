#--------------------------------
# Programming Assignment 2
#
# Name: Nicolas Poitevin
# Date: 10/6/2014
#--------------------------------
#################################
# Exercise P3.14 (7 points)
#card = input("Please enter a card in shorthand notation: ")
#card =card.upper()
#partA=""
#partB=""
#if card[0].isdigit() :
#    partA = card[0]
#    if card[0].startswith('1'):
#        partA = "10"
#elif card.starswith('A'):
#    partA = "Ace"
#elif card.starswith('K'):
#    partA = "King"
#elif card.starswith('Q'):
#    partA = "Queen"
#elif card.starswith('J'):
#    partA = "Jack"
#if card.endswith('D'):
#    partB="Diamonds"
#elif card.endswith('H'):
#    partB="Diamonds"
#elif card.endswith('S'):
#    partB="Spades"
#elif card.endswith('C'):
#    partB="Clubs"
#print(partA+" of "+partB)


#################################
# Exercise P3.17 (7 points)
#string = input("please enter a string :")
#if string.isalpha():
#    print("The string only contains letters")
#if string.isupper():
#    print("The string only contains uppercase letters")
#if string.islower():
#    print("The string only contains lower case letters")
#if string.isdigit():
#    print("The string only contains digits")
#if not string.isdigit() and not string.isalpha():
#    print("The string contains both letters and digits")
#if string[0].isupper():
#    print("The first letter is uppercase")
#if string.endswith('.'):
#    print("The string ends with a period")
    


#################################
# Exercise P3.18 (5 points)
#hour1 = input("Please input the first time: ")
#hour2 = input("Please input the second time: ")
#time1 = ""
#time2 = ""
#if hour1 < hour2:
#    time1 = hour1
#    time2 = hour2
#elif hour1 == hour2:
#    print("They are the same time")
#else:
#    time1 = hour2
#    time2 = hour1
#print(time1+ " comes first and "+time2+" is a bit later.")

#################################
# Exercise P3.19  (6 points)
#string = input("Enter enter a single character: ").upper()
#if len(string) != 1 or string.isdigit():
#    print("ERROR")
#elif string == 'A' or string == 'E' or string == 'I' or string == 'O' or string == 'I' or string == 'U' or string == 'Y':
#    print("Your character is a vowel!")
#else:
#    print("Your character is a constant!")

#################################
# Exercise P3.21 (6 points)
#num1 = float(input("Please input a floating point number:"))
#num2 = float(input("Please input a second floating point number:"))
#if round(num1+.005,2) == round(num2+.005,2):
#    print("The numbers are the same up to two decimal points.")
#else:
#    print("They are different numbers")

#################################
# Exercise P3.25  (6 points)
#status = input("Please input S for single or M for marriaged: ")
#income = int(input("Please enter your income"))
#tax =0
#if status[0].upper == 'S':
#    if income > 0 and income <8000:
#        tax = income * .1
#    elif income > 8000 and income<32000:
#        tax = (income -8000)*.15 +800
#    else:
#        tax= (income -32000)*.25 + 4400
#else:
#    if income>0 and income<16000:
#        tax = income*.1
#    elif income>16000 and income<64000:
#        tax = (income -16000)*.15 +160
#    else:
#        tax = (income -64000)*.25+8800
#print("Your tax is "+str(tax))

#################################
# Exercise Business P3.33 (9 points)
#pin = "1234"
#i =0
#n = False
#while (i<=2 and n == False):
#    i= i+1
#    pinu = input("Please enter your pin: ")
#    if pinu == pin:
#        print("Your pin is correct")
#        n=True
#    elif i == 3:
#        print("Your card is blocked")
#    else:
#        print("Please try again?")
        
#################################
# Exercise Business P3.34 (5 points)
#cost = float(input("Please enter the cost of your groceries: "))
#discount = 0
#if cost > 10 and cost<60:
#    discount = .08
#elif cost>60 and cost<150:
#    discount = .1
#elif cost>150 and cost<210:
#    discount = .12
#elif cost> 210:
#    discount = .14
#print("You win a discount coupon of $ "+str(round(cost*discount,2))+". ("+str(discount)+" of your purchase)")
    
#################################
# Exercise Business P3.35 (6 points)
#level = int(input("Please tell us your statisfaction level 1 = Totally satisfied, 2= Satisfied, 3 = Dissatisfied :"))
#cost =float(input("Please enter the cost of the meal: "))
#tip=0
#if level ==1:
#    tip=.2
#elif level ==2:
#    tip =.15
#elif level ==3:
#    tip=.1
#tip= tip*cost
#print("Your statisfaction level is "+str(level)+" and your tip is %.2f"%tip)
         
#################################
# Exercise Science P3.40 (10 points)
#import math
#n = int(input("Please enter the sound level: "))
#unit =input("What units what that be in dB or Pa?: ").upper
#if unit == "PA" :
#    n=20*math.log(n/(20*10**-6))
#elif n>130:
#    print("Threshold of pain")
#elif n>120:
#    print("Possible hearing damage")
#elif n> 100:
#    print("Jack hammer at 1 m")
#elif n>90:
#    print("Traffic on a busy roadway at 10 m")
#elif n>60:
#    print("Normal conversation")
#elif n>30:
#    print("Calm library")
#else:
#    print("Light leaf rustling")

#################################
# Exercise Science P3.42 (8 points)
#t = float(input("Please enter a temperature in F: "))
#t = (t-32)*5/9+273
#r0 = 33192
#t0 = 40+273
#b = 3310
#r2 = 156300
#r3=r2
#r4=r3
#var =(b*((1/t)-(1/t0)))
#r1=r0*2.71**var
#if (r2/(r1+r2))<(r4/(r3+r4)):
#    print("The alarm will sound")
#else:
#    print("The alarm will not sound")
    
#################################
# Exercise Science P3.43 (8 points)
#m=2
#r=3
#t1=60
#v = int(input("Please enter a velocity: "))
#t= m*v**2/r
#if t1<t:
#    print("The rope will break!")
#else:
#    print("The rope will not break!")

#################################
# Exercise Science P3.44 (9 points)
#r=3
#t=60
#m = int(input("Please enter a mass for the rope"))
#if (m*40**2/r) <t:
#    v=40
#elif (m*20**2/r)<t :
#    v=20
#elif (m*10**2/r)<t:
#    v=10
#elif (m*1**2/r)<t:
#    v=1
#print("The greatest speed that the rope can be spun is "+str(v))

#################################
# Exercise Science P3.45 (8 points)
#g = 6.67E-11
#m = 2.2E14
#r =9.4/2
#ve = (2*g*m/r)**.5
#vl = float(input("Please enter a launch velocity: "))
#if ve < vl:
#    m2 = vl**2*r/(2*g)
#    m2= m2-m
#    print("Halley's Comet needs to be %.2f kg more massive for the jumper to return to the surface"%m2)
#else:
#    print("The jumper will be able to return to the surface")
