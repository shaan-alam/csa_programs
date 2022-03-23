def flip(c):
  if c == '0':
    return '1'
  else:
    return '0'

def onesComplement(bin):
  ones = ""

  for i in range(len(bin)):
    ones += flip(bin[i])

  return ones

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

num = input("Enter binary number: ")

result1 = onesComplement(num)
result2 = twosComplement(num)

print ("Ones Complement : ", result1)
print ("Twos Complement : ", result2)
