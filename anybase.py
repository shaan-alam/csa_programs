def num_to_hex(number):
    if number == 10:
        return "a"
    elif number == 11:
        return "b"
    elif number == 12:
        return "c"
    elif number == 13:
        return "d"
    elif number == 14:
        return "e"
    elif number == 15:
        return "f"
    else:
        return str(number)

def hex_to_dec(number):
    number = number.lower()

    if number == "a":
        return 10
    elif number == "b":
        return 11
    elif number == "c":
        return 12
    elif number == "d":
        return 13
    elif number == "e":
        return 14
    elif number == "f":
        return 15
    else: 
        return int(number)


def r_to_decimal(number, r):
    converted = 0
    power = 0

    one_to_ten = [str(n) for n in range(1, 10)]

    while number != '':
        last = hex_to_dec(number[-1])
        converted += last * (r ** power)
        power += 1
        number = number[:-1]

    return converted

def decimal_to_r(number, r):
    converted = ""

    while number != 0:
        remainder = number % r
        converted += num_to_hex(remainder)
        number //= r

    return converted[::-1]


def convert(a, defualtBase, toBase):
    decimal = r_to_decimal(a, defualtBase)
    result = decimal_to_r(decimal, toBase)

    return result

a = input("Enter a number: ")
defualtBase = int(input("Enter the base: "))
toBase = int(input("Enter the to base: "))

print ("Result = ", convert(a, defualtBase, toBase))

