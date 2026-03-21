print('CALCULATOR')
num1 = float(input('enter the value of num1: '))
operation = input('choose an operator: ')
num2 = float(input('enter the value of num2: '))
if operation == '+' :
    result = num1 + num2
elif operation == '-' :
    result = num1 - num2
elif operation == '*' :
    result = num1 * num2 
elif operation == '/' :
    if num2 == 0 :
     print('error')
    else:
     result = num1 / num2
else:
        print('unknown operation')     
print(f'{num1} {operation} {num2} = {result}')
