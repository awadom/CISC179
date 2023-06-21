try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    number = int(x) / int(y)
    print(number)
# except ZeroDivisionError as err:
#     print(err)
# print("Error: Divided by Zero!")
except ValueError as err:
    print(err)
