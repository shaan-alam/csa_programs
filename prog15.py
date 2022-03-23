# WAP to find selective mask

def selective_mask(a, b):
  result = "" 
  for i in range(len(a)):
    t = "0" if b[i] == "0" else a[i]
    result += t
  
  return result

a = input("Enter first number: " )
b = input("Enter second binary number: ")

print ("Selective Mask : ", selective_mask(a, b))
