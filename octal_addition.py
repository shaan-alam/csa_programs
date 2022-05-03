def octal_addition(a, b):
  i = len(a) - 1
  carry = "0"
  result = ''

  while i >= 0:
    sum = str(int(carry) + int(a[i]) + int(b[i]))
    sum = oct(int(sum))[2:]

    if len(sum) == 2:
      carry = sum[0]
      if i == 0:
        result = sum + result
      else:
        result = sum[1] + result
    else:
      result = sum + result

    i -= 1 

  return result
    

a = input("Enter a octal number: ")
b = input("Ente another octal number: ")

print ("Result = ", octal_addition(a, b))