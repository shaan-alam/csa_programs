def binary_to_decimal(bin):
  pos = len(bin) - 1
  result = 0

  for x in bin:
    result += int(x) * (2 ** pos)
    pos -= 1

  return int(result)

def convert_to_base_4(num):
  decimal = binary_to_decimal(num)

  converted = ""

  while decimal != 0:
    remainder = decimal % 4
    converted = str(remainder) + converted
    decimal //= 4

  return converted

def threesComplement(num):
  result = ""
  
  for x in num:
    result += str(3 - int(x))

  return int(result)

a = input("Enter a binary number: ")

print ("Value in base 4: ", convert_to_base_4(a))
print ("Three's complement: ", threesComplement(convert_to_base_4(a)))
print ("Four's complement: ", threesComplement(convert_to_base_4(a)) + 1)