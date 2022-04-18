def convertToDecimal(num, base):
  l = len(num) - 1
  result = 0

  for i in num:
    result += int(i) * (base ** l)
    l = l - 1

  return result


def convert(num1, defaultBase, toBase):
  decimal = convertToDecimal(num1, defaultBase)
  
  digits = []
  temp = decimal 

  while decimal > 0:
    digit = decimal % toBase
    digits.append(digit)
    decimal //= toBase
  
  digits.reverse()
  result = ""

  for i in digits:
    result += str(i)

  return result



num1 = input("Enter any number: ")
defaultBase = int(input("Enter base: "))

toBase = int(input("Enter base: "))


print ("Result: ", convert(num1, defaultBase, toBase))
