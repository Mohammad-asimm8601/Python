# even check


def even_check(num):
    return num % 2 == 0


result = even_check(4)
print(result)


# Return true if any number is even inside a list


def check_even_list(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list


result = check_even_list([0, 2, 4, 5, 6, 8, 7, 10])
print(result)


stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
for item in stock_prices:
    print(item)


for ticker, price in stock_prices:
    print(price + (0.1 * price))


# Check employee of the month


work_hours = [("abby", 100), ("Billy", 900), ("Cassie", 800)]


def employee_check(work_hours):

    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # return
    return (employee_of_month, current_max)


result = employee_check(work_hours)
name,hours = employee_check(work_hours)
print(result)
print(name)
print(hours)