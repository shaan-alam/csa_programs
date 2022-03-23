# WAP to convert a binary number to decimal number

def convertToDecimal(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += int(i) * pow(2, l)
        l = l - 1
    
    return decimal
    
 
num = input("Enter binary number: ")
print("Decimal Number: ", convertToDecimal(num))
