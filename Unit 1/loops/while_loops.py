total =int(input('Enter a number: '))

while total < 51 or total > 1000 :
      total = int(input('Enter a number: '))

print ('the total is greater than 50: ')

# Inviting people to a party
count = 0
while True:
        name = input("Enter the name of the person for invitation: ")
        print(name + " has been invited.")
        count += 1

        name = input("Is there anyone else you want to invite?: ")
        if name != 'yes':
               print("There are ", str(count),  " people coming to the party.")