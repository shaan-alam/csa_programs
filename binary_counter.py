def decimal(a):
  result = 0

  power = len(str(a)) - 1
  for x in str(a):
    result += int(x) * (2 ** power)
    power -= 1

  return int(result)

def binary(a):
  converted = ""
  temp = int (a)

  while temp != 0:
    remainder = temp % 2
    converted = str(remainder) + converted
    temp //= 2

  return converted


def check (a):
  if a < 0 or a > 11111:
    return False

  return True

a = int(input("Enter a value: "))

if check(a):
  start = decimal(a)
  end = 31

  while start <= end:
    print (binary(start), " - ", start)
    start += 1

