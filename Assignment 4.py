#-------------------------------------------------
# Programming Assignment 4
#
# Name: Nicolas Poitevin Castelo
# Date: 11/25/2014
#
#-------------------------------------------------
##################################################
# Exercise P5.2 (8 points)
def allTheSame(x,y,z):
    if x ==y and x == z:
        return True
    else:
        return False
    
def allDifferent(x,y,z):
    if x != y and x != z and y != z:
        return True
    else:
        return False
    
def sorted(x,y,z):
    if x<=y and y<=z:
        return True
    else:
        return False


##################################################
# Exercise P5.4 (8 points)

def middle(string):
    x = len(string)
    y = x//2
    if x%2 == 0:
        return string[y-1:y+1]
    else:
        return string[y]
        
##################################################
# Exercise P5.5 (8 points)

def repeat(string,n,delim):
    newString = (string + delim)*3
    return newString[0:len(newString)-1]


##################################################
# Exercise P5.7 (8 points)

def countWords(string):
    return 1 + string.count(" ")
    
##################################################
# Exercise P5.8 (8 points)
import random

def scramble(word):
    if len(word) < 4:
        return word
    else:
        x = random.randint(1,len(word)-2)
        y = random.randint(1,len(word)-2)
        while x == y:
            y = random.randint(1,len(word)-2)
        if x < y:
            return concat(x,y,word)
        else:
            return concat(y,x,word)

def concat(x,y,word):
    return word[0:x]+word[y]+word[x+1:y]+word[x]+word[y+1:]
    

##################################################
# Exercise P5.15 (8 points)
end = ""
def reverse(string):
    global end
    if 0 != len(string):
        end += string[len(string)-1]
        string = string[0:len(string)-1]
        return reverse(string)
    else:
        return end
find(
##################################################
# Exercise P5.17 (8 points)

def find(string,match):
    if len(string) != 0:
        if string[0:len(match)] == match:
            return True
        else:
            return find(string[1:],match)
    else:
        return False
def find2(string,match):
    for x in range(len(string)-len(match)-1):
        if string[x:x+len(match) == match:
          return True
    return False
print(find2("miss","iss"))
##################################################
# Exercise Business P5.28 (8 points)

def aid(income,kids):
    if income >= 30000 and income <= 40000 and kids >2:
        return "You will be given $"+str(1000*kids)
    elif income >= 20000 and income <= 30000 and kids >1:
        return "You will be given $"+str(1500*kids)
    elif income < 20000 and kids > 0:
        return "You will be given $"+str(2000*kids)
    else:
        return "No financial aid shall be given."
    
def finance():
    income =int(input("Plese enter your annual income: "))
    kids =int(input("Please enter how many kids you have : "))
    return aid(income,kids)
    

##################################################
# Exercise Business P5.30 (10 points)

def valid(password):
    a = False
    b = a
    c = a
    d = a
    if len(password) > 7 :
        a = True   
    while x in password:
        if x.isupper():
            b = True
        if x.islower():
            c = True
        if x.isdigit():
            d = True
    if (a and b and c and d):
        return True
    else:
        return False
    
def passwordCreate():
    passA = input("Please enter a password that fits the criteria : ")
    passB = input("Please input your password again : ")
    while passA != passB and not valid(passA):
        return passwordCreate()
    else:
        return "Your password has been accepted!"




##################################################
# Exercise Science P5.33 (8 points)

def focalLength(r1,r2,n,d):
    # n = refractive index, d=thickness, r1,r2 = radii of curvature
    return ((n-1)*((1/r1)-(1-r2)+(((n-1)*d)/(n*r1*r2))))**-1



##################################################
# Exercise Science P5.34 (8 points)
from math import pi

def volume(h,r1,r2):
    return (1/3)*pi*h*(r1*r1+r2*r2*r1*r2)

def surfaceArea(h,r1,r2):
    return pi*(r1+r2)*((((r2-r1)**2)+h*h)**(.5))+pi*r1*r1


##################################################
# Exercise Science P5.35 (10 points)
# NOT SURE IF YOU WANTED ME TO IMPORT PI AGAIN FOR THIS EXERCISE.

def diameter(wireGauge):
    return 0.127*(92**((36-wireGauge)/39))
def copperWireResistance(length,wireGauge):
    res = 1.678E-8
    return resFormula(res,length,diameter(wireGauge))
def aluminumWireResistance(length,wireGauge):
    res = 2.82E-8
    return resFormula(res,length,diameter(wireGauge))
def resFormula(p,l,d):
    return (4*p*l)/(pi*d*d)
def testFunctions(): # Doesn't specify how to test the functions.
    gauge = float(input("Please enter a gauge for your wire : "))
    length = float(input("Please enter how long your wire is : "))
    copper = input("Is your wire copper \"Y\" or \"N\" ? ")
    aluminum =input("Is your wire aluminum \"Y\" or \"N\" ? ")
    if copper.upper() == 'Y':
        x = copperWireResistance(length,gauge)
    elif aluminum.upper() == 'Y':
        x = aluminumWireResistance(length,gauge)
    else: 
        res = float(input("Sorry the resistivity for your wire is not found please input : "))
        x = resFormula(res,length,gauge)
    return "Your resistance is "+str(x)+"Ω!"

##################################################
def main():
    print()

if __name__ == '__main__':
    main()
