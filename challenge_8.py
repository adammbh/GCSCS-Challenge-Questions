time = 0
texts = 0

# total bill cost = 0.10 per minute
# total bill cost = 0.05 per text
# additional monthly charge = 10.00

time = int(input('Please write the amount of minutes you have used in the last month: '))
texts = int(input('Please write the amount of texts you have sent in the last month: '))

timetotal = 0.10 * time
textstotal = 0.05 * texts

finaltotal = timetotal + textstotal + 10

print('Your final total is: ' + str(finaltotal))