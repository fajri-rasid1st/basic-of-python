# Exceptions

for i in range(int(input())):
    numbers = input().split()
    try:
        print(int(numbers[0]) // int(numbers[1]))
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)
