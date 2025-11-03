print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponent")
print("7. Square Root")
print("8. Increment")
print("9. Decrement")
try:
    option = int(input('Choose an Operation: '))
    result = 0
except:
    print("Invalid Input. Please enter an integer.")
else:
    if (option in [1,2,3,4,5,6,]):
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
    elif (option in [7,]):
        if (option == 7):
              num = float(input("Enter a number: "))
              result = num ** 0.5
    elif (option in [8,9]):
        num = int(input('Enter a Number: '))
        if (option == 8):
           num += 1
           result = num
        elif(option == 9):
           num -= 1
           result = num 
    else:
     print("Invalid Number")
print("The Result of the operation is: {}".format(result))
