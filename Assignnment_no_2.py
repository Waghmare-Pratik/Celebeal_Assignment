def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

def percentage(x, y):
    return (x * y) / 100

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Percentage")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        numbers = [float(num) for num in input("Enter numbers separated by space: ").split()]

        if choice == '1':
            print("Result:", add(numbers))
        elif choice == '2':
            print("Result:", subtract(numbers))
        elif choice == '3':
            print("Result:", multiply(numbers))
        elif choice == '4':
            print("Result:", divide(numbers))
        elif choice == '5':
            num1 = numbers[0]
            num2 = numbers[1]
            print("Result:", percentage(num1, num2))
        break
    else:
        print("Invalid Input")
