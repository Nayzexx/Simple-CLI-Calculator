while True:
 try:
      a= float(input('number_1: '))
      b= float(input("number_2: "))
      op = input("operation: ")
      if op == "+":
          print("result:", a + b)
      elif op == "-":
          print('result:', a - b)
      elif op == "*":
          print('result:', a * b)
      elif op == "/":
          print('result:', a / b)
      elif op == "**":
          print('result:', a ** b)
      elif op == "//":
          print('result:', a // b)
      elif op == "%":
          print('result:', a % b)
      else:
          print("I don't know what you are doing")
          continue
 except ValueError:
     print('It is not a number')
     continue
 except ZeroDivisionError:
       print("You can't divide by zero")
       continue
 cont=input("Continue? (yes/no): ? ")
 if cont == ('yes'):
      continue
 elif cont == ('no'):
      break