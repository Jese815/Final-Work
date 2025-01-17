#1
list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

#2
collumn=int(input('What collumn do you want to pick from? (0-3)'))

row=int(input('What row do you want to pick from?(0-2)'))

print(list[collumn][row])

#3
prow=int(input('Which row would you like displayed?'))
print(list[prow])

addrow=int(input('Enter a new value to add to the row.'))
list[prow].append(addrow)

print(list[prow])

#4
row2=int(input('Which row would you like displayed? '))
print(list[row2])
collumn2=int(input('Which collumn in that row would you like shown? '))
updatedlist=list[row2][collumn2]
print(list[row2][collumn2])
change=input('Would you like to change that value?(Y or N)')
if change == 'Y' or 'y':
    numchange=int(input('What value?'))
    list.insert(collumn2,numchange)

print('Updated:',list[row2])

#5
sales=dict()
sales = {"Levi":{"N":3056,"S":8463,"E":8441,'W':2694},
            "Andy":{"N":4832,"S":6786,"E":4737,'W':3612},
            "Clara":{"N":5239,"S":4802,"E":5820,'W':1859},
            "Jese":{"N":3904,"S":3645,"E":8821,'W':2451}}



#6
name=input('Give me a name (dont forget capitals pls)')
region=input('Give me a region (NSEW) (dont forget capital pls)')
print(sales[name][region])
namechange=input('Give me a name youd like to change')
regionchange=input('Give me a region from that name that you want to change (NSEW) (dont forget capital pls)')
changingname=input('What do you want to change the name to?')
changingregion=input('What do you want to change the region to?')
numchangeregion=input('What number?')

del sales [namechange]
sales[changingname]=changingregion,numchangeregion
print(sales)