# WAP Convert decimal to binary

def convertToBinary(num):
    a = []
    temp = num

    while temp > 0:
        digit = temp % 2
        a.append(digit)
        temp //= 2
    
    a.reverse()

    result = 0
    for i in a:
        result = result * 10 + i
    
    return result

num = int(input("Enter a decimal number: "))
print ("Binary of", num," is = ", convertToBinary(num))