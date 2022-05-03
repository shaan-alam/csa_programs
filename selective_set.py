def selective_set(a, b):
  result = ""

  for x in range(0, len(a)):
    if b[x] == "1":
      result += "1"
    else: 
      result += a[x]
    
  return result

a = input("Enter a binary number: ")
b = input("Enter a binary number: ")

print ("Result: ", selective_set(a, b))