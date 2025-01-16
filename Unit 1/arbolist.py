import math

try:

    friend_height = 1.65

    x = int(input('Enter the angle: '))
    x = math.degrees (x*0.75)

    tree = math.tan (x * friend_height)
    print('This is the height of the tree', tree)

except(ZeroDivisionError):
    print("That isn't a valid answer")