# Q7
def twosComplement(bin):
  i = len(bin) - 1

  while i >= 0:
    if (bin[i] == '1'):
      break
    i -= 1

  if i == -1:
    return '1' + bin
  
  k = i - 1
  str = list(bin)
  
  while k >= 0:
    if str[k] == '1':
      str[k] = '0'
    else:
      str[k] = '1'

    k-=1

  result = ""

  for i in str:
    result += i

  return result

def dec_to_bin(num):
    a = []
    temp = int(num)

    while temp > 0:
        digit = temp % 2
        a.append(digit)
        temp //= 2
    
    a.reverse()

    result = 0
    for i in a:
        result = result * 10 + i
    
    return result

def binary_addition(a, b):
  i = len(a) - 1
  result = ""
  
  carry = "0"

  while i >= 0:
    sum = dec_to_bin(int(carry) + int(a[i]) + int(b[i]))
    
    print ('sum', sum)

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
  

print (binary_addition("001", "101"))

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

print ("A = ", a)
print ("B = ", b)

