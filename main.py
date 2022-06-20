def multiply(a, b):
    return a * b


def total(account):
    sum = 0
    for money in account:
        sum += money
    return sum


result = multiply(-3, 9)
print(result)

my_account = [50.50, 25, -40, 150]
my_money = total(my_account)
print(my_money)
