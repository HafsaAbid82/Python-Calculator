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
    exit()
else:
    if (option in [1,2,3,4,5,6]):
        try:
            num1 = int(input('Enter First Number: '))
            num2 = int(input('Enter Second Number: '))
            if (option == 1):
                result = num1 + num2
            elif(option == 2):
                result = num1 - num2
            elif(option == 3):
                result = num1 * num2
            elif(option == 4):
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 // num2
            elif(option == 5):
                result = num1 % num2
            elif(option == 6):
                result = num1 ** num2
        except:
            print("Invalid Input. Please enter valid numbers.")
    elif (option in [7]):
        try:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Error: Cannot take square root of a negative number.")
            else:
                result = num ** 0.5
        except:
            print("Invalid Input. Please enter a valid number.")   
    elif (option in [8,9]):
        try:
            num = int(input('Enter a Number: '))
            if (option == 8):
                num += 1
                result = num
            elif(option == 9):
                num -= 1
                result = num 
        except:
            print("Invalid Input. Please enter an integer.")
    else:
        print("Invalid Number")
print("The Result of the operation is: {}".format(result))

