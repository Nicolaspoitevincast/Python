#-------------------------------------------------
# Programming Assignment 5
#
# Name: Nicolas Poitevin
# Date: 12/9/2014
#
#-------------------------------------------------
##################################################
# Exercise P6.17 (20 points)
from random import randint
def exercise_P6_17():
    print()
    print('Exercise P6.17')
    list1= []
    list2 =[]
    for y in range(10):
        list1[:]=[]
        for x in range(1,11):
            list2.append(x)
        while len(list2) != 0:
            x = randint(0,len(list2)-1)
            list1.append(list2[x])
            list2.remove(list2[x])
        print(list1)
    print()

##################################################
# Exercise P6.19 (20 points)

def exercise_P6_19():
    print()
    print('Exercise P6.19')
    iDeck = 45
    piles =[]
    iPiles = randint(2,9)
    for a in range(iPiles):
        pile = randint(1,iDeck)
        if iDeck > pile:
            piles.append(pile)
            iDeck=iDeck-pile
    if iDeck != 0:
        piles.append(iDeck)
    print(piles)
    while not end(piles):
        y=len(piles)
        for x in range(y):
            piles[x]= piles[x]-1
        piles.append(y)
        for x in range(piles.count(0)):
            piles.pop(piles.index(0))
        print(piles)   
    print()

def end(piles):
    t2=0
    for t1 in range(1,10):
        if piles.count(t1)==1:
            t2 +=1
    if t2 == 9:
        return True
    else:
        return False
    
##################################################
# Exercise P6.22 (20 points)

def exercise_P6_22():
    print()
    print('Exercise P6.22')
    values= fillTable()
    for a in values:
        print(a)
    row = int(input("Please input the row you want to use? "))
    column = int(input("Please input the column you want to use? "))
    print(neighborAverage(values,row,column))
    print()

def fillTable(r=3,c=3,rand=9):
    listA=[]
    for y in range(r):        
        listA.append(fillList(c,rand))
    return listA

def fillList(c,rand=9):
    listB=[]
    for x in range(c):
        listB.append(randint(0,rand))
    return listB

def neighborAverage(values,r,c):
    total = 0
    i=0
    colomn = len(values[0])-1
    row = len(values)-1
    if r > 0:
        total= total +values[r-1][c]
        i+=1
    if r < row:
        total = total + values[r+1][c]
        i+=1
    if c > 0:
        total += values[r][c-1]
        i+=1
    if c < colomn:
        total += values[r][c+1]
        i+=1
    if c!=0 and r!=0:
        total +=values[r-1][c-1]
        i+=1
    if c!=colomn and r!=0:
        total +=values[r-1][c+1]
        i+=1
    if c != 0 and r!=row:
        total+=values[r+1][c-1]
        i+=1
    if r!=row and c!=colomn:
        total+=values[r+1][c+1]
        i+=1
    return total//i 


##################################################
# Exercise P6.30 (20 points)

def exercise_P6_30():
    print()
    print('Exercise P6.30')
    a= sorted(fillList(5)) 
    b= sorted(fillList(4))
    print(a)
    print(b)
    c = mergeSorted(a,b)
    print(c)
    print()
    
def mergeSorted(a,b):
    indexA =0
    indexB =0
    c=[]
    while len(a) !=indexA and len(b)!=indexB:
        if a[indexA] < b[indexB]:
            c.append(a[indexA])
            indexA +=1
        else:
            c.append(b[indexB])
            indexB +=1
    if len(a) != indexA:
        c+=a[indexA:]
    if len(b) != indexB:
        c+=b[indexB:]
    return c
    

##################################################
# Exercise Science P6.35 (20 points)

def exercise_P6_35():
    print()
    print('Exercise Science P6.35')
    heights =fillTable(10,10,100)
    for x in range(0,11):
        waterLevel = x*10
        print("Water Level :",waterLevel)
        floodMap(heights,waterLevel)
    print()

def floodMap(heights,waterLevel):
    for y in range(len(heights)):
        for x in range(len(heights[y])):
            if heights[y][x] < waterLevel:
                print("*",end="")
            else:
                print(" ",end="")
        print()

##################################################
def main():
    pass
    

if __name__ == '__main__':
    main()
