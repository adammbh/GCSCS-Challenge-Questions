num1 = 0
num2 = 0

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if num1 < num2:
    print('The bigger number is: ' + str(num2))
elif num1 > num2:
    print('The bigger number is: ' + str(num1))
else:
    print('Both the numbers are the same')