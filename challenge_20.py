customerDataOne = [
    "Smith J.",
    "5",
    "7",
    "1",
    False
]

customerDataTwo = [
    "William P.",
    "10",
    "12",
    "3",
    True
]

# Customer One
cusOneNum1 = int(customerDataOne[1])
cusOneNum2 = int(customerDataOne[2])
cusOneNum3 = int(customerDataOne[3])
cusOneTotal = cusOneNum1 + cusOneNum2 + cusOneNum3

# Customer Two
cusTwoNum1 = int(customerDataTwo[1])
cusTwoNum2 = int(customerDataTwo[2])
cusTwoNum3 = int(customerDataTwo[3])
cusTwoTotal = cusTwoNum1 + cusTwoNum2 + cusTwoNum3

if (cusOneTotal > 20):
    print('Added loyalty program to customer one')
elif (cusTwoTotal > 20):
    print('Added loyalty program to customer two')
else:
    print('All the customers do not have 20 or more pizzas')