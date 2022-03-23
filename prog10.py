# WAP to convert a number from one base to another base.

def convert(num, numBase, toBase):
    result = 0
    power = 0
    temp = num

    while temp != 0:
        result += (temp % toBase) * (numBase ** power)
        power += 1
        temp //= toBase
    
    return result

choice = "Y"

while choice == "Y" or choice == 'y':
    num = int(input("Enter Number: "))  
    numBase = int(input("Enter number base: "))          
    toBase = int(input("Enter to base: "))

    print ("Number in Base ", numBase, ": ", num)
    print ("Number in Base ", toBase, ": ", convert(num, numBase, toBase) )
    
    choice = input("Do you wish to continue?? [Y/N]")
    print ("\n")





