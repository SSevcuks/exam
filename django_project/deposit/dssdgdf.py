deposit = 1000
term = 2
rate = 0.05

interest = 0
for i in range(term):
    deposit = deposit + interest
    interest = interest + deposit * 0.05
    print(deposit)
print(interest)