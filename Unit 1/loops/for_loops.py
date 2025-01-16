number = int(input("Enter a number between 1 and 12: "))

while number < 1 or number > 12:
        print("Please enter a number within the range.")
        number = int(input("Enter a number between 1 and 12: "))

print("Times table for " + str(number))
for i in range(1, 13):
        print(number, "x", i, "=", number * i)

# Enter 5 number and display
total = 0

for i in range(5):
        number = float(input("Enter number " + str(i + 1) + ": "))
        include = input("Do you want to include this number? (y/n): ")

if include == 'yes':
    total += number