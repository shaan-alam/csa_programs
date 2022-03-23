# WAP to find selective complement

def selective_complement(a, b):
  result = ""
  
  for i in range(len(a)):
    t = "1" if a[i] != b[i] else "0"
    result += t
  
  return result

a = input("Enter first number: " )
b = input("Enter second binary number: ")

print ("Selective Complement : ", selective_complement(a, b))
