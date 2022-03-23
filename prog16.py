# WAP to find selective set

def selective_set(a, b):
  result = "" 

  for i in range(len(a)):
    x = "0" if b[i] == "1" else a[i]
    result += x

  return result

a = input("Enter first number: " )
b = input("Enter second binary number: ")

print ("Selective Set : ", selective_set(a, b))
