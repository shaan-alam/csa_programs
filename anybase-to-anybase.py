conversion_table = {
  'a': 10,
  'b': 11,
  'c': 12,
  'd': 13,
  'e': 14,
  'f': 15,
  '10': 'a',
  '11': 'b',
  '12': 'c',
  '13': 'd',
  '14': 'e',
  '15': 'f'
}

def hex_to_num(number):
  if number in conversion_table:
    return int(conversion_table[number.lower()])
  else:
    return int(number)


def num_to_hex(number):
  if number in conversion_table:
    return conversion_table[number]
  else:
    return str(number)
  # return conversion_table[number] if number in conversion_table else str(number)

def r_to_decimal(number, defaultBase):
  converted = 0
  power = 0

  while number != '':
    last = hex_to_num(number[-1])
    converted += last * (defaultBase ** power)
    power += 1
    number = number[:-1]

  return converted

def decimal_to_r(number, toBase):
  converted = ""
  
  while number != 0:
    remainder = number % toBase
    converted += num_to_hex(str(remainder))
    number //= toBase
  
  return converted[::-1]

def convert(number, defaultBase, toBase):
  decimal = r_to_decimal(number, defaultBase)
  result = decimal_to_r(decimal, toBase)

  return result

number = input("Enter a number: ")
defaultBase = int(input("Enter default base: "))
toBase = int(input("Enter the to base: "))

print ("Result: ", convert(number, defaultBase, toBase))