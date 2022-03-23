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

conversion_dec_to_hex = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def dec_to_hex(num):
    a = []
    temp = int(num)

    while temp > 0:
        digit = temp % 16
        if (digit > 9): 
            digit = conversion_dec_to_hex[digit]
        a.append(digit)
        temp //= 16
    
    a.reverse()

    result = ""
    for i in a:
        result += str(i)
    
    return result

def binary_to_dec(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += int(i) * pow(2, l)
        l = l - 1
    
    return decimal
    
def octal_to_dec(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += int(i) * pow(8, l)
        l = l - 1
    
    return decimal

conversion_hex_to_dec = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def hex_to_dec(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += conversion_hex_to_dec[i.upper()] * pow(16, l) 
        l = l - 1
    
    return decimal

while True:
  print ("1. Decimal to binary.")
  print ("2. Decimal to octal")
  print ("3. Decimal to Hexadecimal")
  print ("4. Binary to Decimal")
  print ("5. Octal to Decimal")
  print ("6. Hexadecimal to Decimal")
  print ("7. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    num = input("Enter decimal number: ")

    if not int(num):
        print ("Please enter decimal number")
    else:
        print ("Binary number = ", dec_to_bin(num))
  elif choice == 2:
    num = input("Enter decimal number: ")
    print ("Octal number = ", dec_to_octal(num))
  elif choice == 3:
    num = input("Enter decimal number: ")
    print ("Hexadecimal number = ", dec_to_hex(num))
  elif choice == 4:
    num = input("Enter Binary number: ")
    print ("Decimal number = ", binary_to_dec(num))
  elif choice == 5:
    num = input("Enter Octal number: ")
    print ("Decimal number = ", octal_to_dec(num))
  elif choice == 6:
    num = input("Enter hexadecimal number: ")
    print ("Decimal number = ", hex_to_dec(num))
  elif choice == 7:
    break