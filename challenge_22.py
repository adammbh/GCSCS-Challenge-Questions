totalmarks = 0

totalmarks = int(input('What is your total mark out of a 100?'))

# >= greater than or equal to

if(totalmarks <= 0):
    print('You got a U')
elif(totalmarks <= 10):
    print('You got a grade 1')
elif(totalmarks <= 20):
    print('You got a grade 2')
elif(totalmarks <= 30):
    print('You got a grade 3')
elif(totalmarks <= 40):
    print('You got a grade 4')
elif(totalmarks <= 50):
    print('You got a grade 5')
elif(totalmarks <= 60):
    print('You got a grade 6')
elif(totalmarks <= 70):
    print('You got a grade 7')
elif(totalmarks <= 80):
    print('You got a grade 8')
elif(totalmarks >= 90):
    print('You got a grade 9')    
else:
    print('You got a U')