print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
option = int(input('Choose an Operation: '))
result = 0

if (option in [1,2,3,4]):
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))
    if (option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2
    elif(option == 5):
        result = num1 % num2
    elif(option == 6):
        result = num1 ** num2
else:
    print("Invalid Number")
print("The Result of the operation is: {}".format(result))
