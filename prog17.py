# WAP To perform octal addition and substraction

def if_octal(a):
  for i in a:
    if int(i) > 7 or int(i) < 0:
      return False

  return True

def eight_complement(a):
  a = list(a)
  
  length = len(a)

  for i in range(length):
    a[i] = str(7 - int(a[i]))
  
  a[length - 1] = str(int(a[length - 1]) + 1)

  result = ""

  for i in a:
    result += i
  
  return result


def dec_to_octal(num):
  a = []
  temp = int(num)

  while temp > 0:
    digit = temp % 8
    a.append(digit)
    temp //= 8
  
  a.reverse()

  result = 0
  for i in a:
      result = result * 10 + i
  
  return result


def octal_addition(a, b):
  i = len(a) - 1
  result = ""
  
  carry = "0"

  while i >= 0:
    sum = dec_to_octal(str(int(carry) + int(a[i]) + int(b[i])))
    
    if len(str(sum)) == 2:
      carry = str(sum)[0]
      if i == 0:
        result = str(sum) + result
      else:
        result = str(sum)[1] + result
    else:
      result = str(sum) + result

    i -= 1
  
  return result
  
def octal_substraction(a, b):
  i = len(a) - 1
  result = ""
  
  a = list(a)
  b = list(b)

  carry = ""

  while i >= 0:

    if int(a[i]) < int(b[i]):
      carry = str(int(a[i]) + 8)
      a[i - 1] = str(int(a[i - 1]) - 1)
      difference = int(carry) - int(b[i])
      result = str(difference) + result
    else:
      difference = int(a[i]) - int(b[i])
      result = str(difference) + result
    
    i -= 1
  
  return result


while True:
  print ("\n=========MENU=========\n")
  print ("1. Octal Addition")
  print ("2. Octal Substraction")
  print ("3. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    num1 = input("Enter first octal number: ")
    num2 = input("Enter second octal number: ")
    
    if if_octal(num1) and if_octal(num2):
      print ("Octal addition = ", octal_addition(num1, num2))
    else:
      print ("Please provide octal numbers!!\n")
    
  elif choice == 2:
    num1 = input("Enter first octal number: ")
    num2 = input("Enter second octal number: ")
    
    if if_octal(num1) and if_octal(num2):
      if int(num1) < int(num2):
        eight_comp = eight_complement(num2)
        sum = octal_addition(num1, eight_comp)
        result = "-" + eight_complement(sum)
        print ("Octal Substraction = ", result)
      else:
        print ("Octal Substraction = ", octal_substraction(num1, num2))
    else:
      print ("Please provide octal numbers!!\n")

  elif choice == 3:
    break 
  else:
    print ("Wrong choice!!")

