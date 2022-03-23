# WAP to convert a decimal number to octal number

def convertToOctal(num):
    a = []
    temp = num

    while temp > 0:
        digit = temp % 8
        a.append(digit)
        temp //= 8
    
    a.reverse()

    result = 0
    for i in a:
        result = result * 10 + i
    
    return result

num = int(input('Enter a decimal number: '))
print ("Octal numer: ", convertToOctal(num))


        
    