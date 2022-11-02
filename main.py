# Program make a simple calculator

from curses.ascii import isdigit
from package import calculator
from package import log
import logging

# success, fail logger 생성
success_logger = log.get_logging("success", logging.DEBUG, './logs/success.log')
fail_logger = log.get_logging("fail", logging.ERROR, './logs/fail.log')

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
        
        try :
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            log_str = "Invalid Input: 숫자만 입력 가능합니다."
            fail_logger.error(log_str)
            print(log_str)
            continue
      
        # 더하기
        if choice == '1':
            log_str = '%0.1f + %0.1f = %0.1f' % (num1, num2, calculator.add(num1, num2))
            print(log_str)
            success_logger.debug(log_str)

        # 빼기
        elif choice == '2':
            log_str = '%0.1f - %0.1f = %0.1f' % (num1, num2, calculator.subtract(num1, num2))
            print(log_str)
            success_logger.debug(log_str)

        # 곱하기
        elif choice == '3':
            log_str = '%0.1f * %0.1f = %0.1f' % (num1, num2, calculator.multiply(num1, num2))
            print(log_str)
            success_logger.debug(log_str)

        # 나누기
        elif choice == '4':
            value = calculator.divide(num1, num2)

            # 나누기 에러
            if value == False:
                log_str = "Div By Zero: 0으로 나눌 수 없습니다."
                fail_logger.error(log_str)

            else:
                log_str = '%0.1f / %0.1f = %0.1f' % (num1, num2, value)
                success_logger.debug(log_str)
            
            print(log_str)


        # check if user wants another calculation
        # break the while loop if answer is no

        out_while_condi = True
        break_val = False

        # 프로그램 종료 루틴에서, yes/no 이외의 입력에 대해 재확인 하기 위해 while loop 사용
        while out_while_condi:
            
            # yes/no 입력값에 대해 대소문자 모두 허용하기 위해 입력값을 전부 소문자로 변경
            next_calculation = input("Let's do next calculation? (yes/no): ").lower()
            out_while_condi = False

            if next_calculation == "yes":
                continue

            elif next_calculation == "no":
                
                inner_while_condi = True
 
                # 프로그램 종료 전 종료 재확인에서 yes, no 이외의 값이 들어오면 다시 재확인 하기 위해 while loop 사용
                while inner_while_condi:
                    again_check = input("Are you sure? (yes/no): ").lower()
                
                    inner_while_condi = False

                    if again_check == "yes":
                        break_val = True

                    elif again_check == "no":
                        continue

                    else:
                        log_str = "Invalid Input: yes/no 중 하나의 값을 입력해 주세요."
                        fail_logger.error(log_str)
                        print(log_str)
                        inner_while_condi = True
            
            else:           
                log_str = "Invalid Input: yes/no 중 하나의 값을 입력해 주세요."
                fail_logger.error(log_str)
                print(log_str)
                out_while_condi = True

        if break_val == True:
            break
    else:
        log_str = "Invalid Input: 1~4 사이의 값을 입력해 주세요."
        fail_logger.error(log_str)
        print(log_str)
