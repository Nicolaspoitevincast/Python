#--------------------------------
# Programming Assignment 1
#
# Name: Nicolas Poitevin
# Date: 9/22/2014
#
#--------------------------------
# Exercise P2.4 (7 points)
#int1 = int(input("Please input the first integer :"))
#int2 = int(input("Please input the second interger :"))
#print("Sum: ", int1+int2)
#print("Difference: ", int1-int2)
#print("Product: ", int1*int2)
#print("Average: ", (int1+int2)/2)
#print("Distance: ", abs(int1-int2))
#print("Maximum: ", max(int1,int2))
#print("Minimum: ", min(int1,int2))

#################################
# Exercise P2.5 (4 points)
#int1 = int(input("Please input the first integer :"))
#int2 = int(input("Please input the second interger :"))
#print("%-15s"%("Sum:"),(int1+int2))
#print("%-15s"%("Difference:") ,(int1-int2))
#print("%-15s"%("Product:") ,(int1*int2))
#print("%-15s"%("Average:"),((int1+int2)/2))
#print("%-15s"%("Distance:") ,(abs(int1-int2)))
#print("%-15s"%("Maximum:"),(max(int1,int2)))
#print("%-15s"%("Minimum:") ,(min(int1,int2)))


#################################
# Exercise P2.7 (4 points)
#from math import pi
#radius = int(input("Please inter the radius:"))
#print("The area of a circle with that radius is: %.2f"%(pi*radius*radius))
#print("The circumference of a circle with that radius is: %.2f"%(radius*2*pi))
#print("The volume of a sphere with that radius is: %.2f"%(radius*radius*radius*pi*3/4))
#print("The surface area of a sphere with that radius is: %.2f"%(4*pi*radius*radius))

#################################
# Exercise P2.13 (7 points)
#numberString = input("Please enter an interger between 1,000 and 999,999 : ")
#index = numberString.index(',')
#numberInt = int(numberString[0:index]+numberString[index+1:len(numberString)])
#print(numberInt)

#################################
# Exercise P2.14 (7 points)
#number = input("Please enter an interger between 1,000 and 999,999 : ")
#index = len(number)-3
#numberString = number[0:index]+","+number[index:len(number)]
#print(numberString)

#################################
# Exercise P2.16 (7 points)
#time1= int(input("Please input the first time in military format: "))
#time2= int(input("Please input the second time in military format: "))
#timeDifference = str("%04d"%(abs(time1-time2)))
#print(int(timeDifference[0:2])," hours ",int(timeDifference[2:4])," minutes ")

#################################
# Exercise P2.21 (10 points)
#y = int(input("Please insert a year: "))
#a = y%19
#b = y/100
#c = y%100
#d = b/4
#e = b%4
#g = (8*b+13)/25
#h = (19*a+b-d-g+15)/30
#j = c/4
#k = c%4
#m = (a+11*h)/319
#r = (2 * e + 2 * j - k - h + m + 32)%7
#n = (h - m + r + 90)/25
#p = (h- m + r + n + 19)*10%32
#print("Easter Sunday fell on",int(n),"/",int(p))


#################################
# Exercise P2.22 (7 points)
#string = input("Please enter a string: ")
#print(string[0:3],"...",string[len(string)-3:len(string)])

#################################
# Exercise Business P2.33 (8 points)
#bookPrice = int(input("Please input the total book price: "))
#bookNum = int(input("Please input the number of purchased books: "))
#tax = bookPrice*.0075
#shipping = bookNum*2
#total =bookPrice+tax+shipping
#print("%.2f"%total)


#################################
# Exercise Business P2.35 (8 points)
#due=float(input("What is the amount due: "))
#recieved=float(input("What is the amount recieved: "))
#change = recieved - due
#dollars = int(change//1)
#change = int(round((change-dollars)*100))
#quarters = change//25
#change = change - quarters*25
#dimes = change//10
#change = change -dimes*10
#nickels = change//5
#change = change - nickels*5
#print("Dollars returned: ",dollars)
#print("Quarters returned: ",quarters)
#print("Dimes returned: ",dimes)
#print("Nickels returned: ",nickels)
#print("Pennies returned: ",change)

#################################
# Exercise Science P2.38 (8 points)
#resistance1 = float(input("Please enter the first resistance: "))
#resistance2 = float(input("Please enter the second resistance: "))
#resistance3 = float(input("Please enter the third resistance: "))
#resistanceTotal = resistance1 + (1/resistance2 +1/resistance3)**-1
#print("The total resistance in this circuit is: ",resistanceTotal)


#################################
# Exercise Science P2.39 (8 points)
#from math import log,e
#t = float(input("Please input the tempurature in celisius: "))
#RH = float(input("Please input a relative humidity between 0 and 1: "))
#a =17.27
#b = 237.7
#f = ((a*t)/(b+t))+(log(RH)/log(e))
#tDew =(b*f)/(a-f)
#print("The dew point temperature is : %.2f "%tDew)


#################################
# Exercise Science P2.40 (8 points)
#from math import log,e
#r = float(input("Please enter the resisntance for the thermistor : "))
#r0 = 1075
#t0= 85
#B = 3969
#t = ((B*t0)/(t0*(log(r/r0)/log(e))+B))-273.15
#print("The liquid temperature in celisius is : %.2f"%t)

#################################
# Exercise Science P2.43 (7 points)
#from math import pi
#q1 = float(input("Please enter the first charge in colulombs : "))
#q2 = float(input("Please enter the second charge in colulombs : "))
#r =float(input("Please enter the distance in meters : "))
#e = 8.854E-12
#f = (q1*q2)/(4*pi*e*r*r)
#print("The force on the charged particles is : %.2f"%f)
