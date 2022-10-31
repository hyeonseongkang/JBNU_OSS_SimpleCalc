# Program make a simple calculator

from package import calculator

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", calculator.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", calculator.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", calculator.multiply(num1, num2))
            
        elif choice == '4':
            value = calculator.divide(num1, num2)
            if value == False:
                print("***Warning***\ndiv by zero")
            else:
                print(num1, "/", num2, "=", value)


        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()

        if next_calculation == "yes":
            continue
        elif next_calculation == "no":
            again_check = input("Are you sure? (yes/no): ").lower()
            if again_check == "yes":
                break
            elif again_check == "no":
                continue
        else:

            continue

    else:
        print("Invalid Input")
