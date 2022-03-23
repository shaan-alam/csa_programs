# WAP to convert a decimal to hexadecimal number

conversion = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def convertToHex(num):
    a = []
    temp = num

    while temp > 0:
        digit = temp % 16
        if (digit > 9): 
            digit = conversion[digit]
        a.append(digit)
        temp //= 16
    
    a.reverse()

    result = ""
    for i in a:
        result += str(i)
    
    return result


        
num = int(input("Enter a number: "))
print("Hexadecimal number: ", convertToHex(num))