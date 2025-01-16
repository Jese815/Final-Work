num1 = int(input('Enter starting number: '))
num2 = int(input('Enter starting number: '))

if num1 < num2: 
    for i in range (num1,num2):
        print (i)
    
    else:
        print ('First number cannot be larger than second number')

user = int(input('Enter a number: '))

while True:
    num1 = input('Double number? (yes or no): ')

    if num1 == 'yes':
        user *= 2
        print ('This is the multipled amount', user)
    
    elif num1 == 'n': 
        num1 == False
        break
    else:
        print ('This not an answer, please choose "yes" or "no" ,')