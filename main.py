# Program make a simple calculator

from package import calculator
from package import log
import logging

success_logging = log.get_logging("success", logging.DEBUG, './logs/success.log')
fail_logging = log.get_logging("fail", logging.ERROR, './logs/fail.log')


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
            print('1')
            log_str = '%0.1f + %0.1f = %0.1f' % (num1, num2, calculator.add(num1, num2))
            success_logging.debug(log_str)


        elif choice == '2':
            print('2')
            log_str = '%0.1f - %0.1f = %0.1f' % (num1, num2, calculator.subtract(num1, num2))
            success_logging.debug(log_str)


        elif choice == '3':
            print('3')
            log_str = '%0.1f * %0.1f = %0.1f' % (num1, num2, calculator.multiply(num1, num2))
            success_logging.debug(log_str)

            
        elif choice == '4':
            print('4')
            value = calculator.divide(num1, num2)
            if value == False:
                log_str = "Div By Zero"
                fail_logging.error(log_str)

            else:
                log_str = '%0.1f / %0.1f = %0.1f' % (num1, num2, value)
                success_logging.debug(log_str)


        # check if user wants another calculation
        # break the while loop if answer is no

        out_while_condi = True
        break_val = False

        while out_while_condi:
            
            next_calculation = input("Let's do next calculation? (yes/no): ").lower()
            out_while_condi = False

            if next_calculation == "yes":
                continue

            elif next_calculation == "no":
                
                inner_while_condi = True
 
                while inner_while_condi:
                    again_check = input("Are you sure? (yes/no): ").lower()
                
                    inner_while_condi = False

                    if again_check == "yes":
                        break_val = True
                    elif again_check == "no":
                        continue
                    else:
                        inner_while_condi = True
            
            else:          
                out_while_condi = True

        if break_val == True:
            break
    else:
        log_str = "Invalid Input"
        fail_logging.error(log_str)
