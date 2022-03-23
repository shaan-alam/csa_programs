# WAP To convert octal to decimal number

def convertToDecimal(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += int(i) * pow(8, l)
        l = l - 1
    
    return decimal

num = input('Enter a octal number: ')
print("Decimal Number: ", convertToDecimal(num))
