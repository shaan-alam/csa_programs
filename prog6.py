# WAP to convert a hexadecimal to decimal number

conversion = {
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

def convertToDecimal(num):
    l = len(num) - 1
    decimal = 0

    for i in num:
        decimal += conversion[i.upper()] * pow(16, l) 
        l = l - 1
    
    return decimal

hex = input("Enter the hexadecimal number: ")
print ("Decimal number: ", convertToDecimal(hex))