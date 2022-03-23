def selective_complement(a, b):
  result = ""
  
  for i in range(len(a)):
    t = "1" if a[i] != b[i] else "0"
    result += t
  
  return result

def selective_clear(a, b):
  result = "" 

  for i in range(len(a)):
    x = "0" if b[i] == "1" else a[i]
    result += x

  return result

def selective_mask(a, b):
  result = "" 
  for i in range(len(a)):
    t = "0" if b[i] == "0" else a[i]
    result += t
  
  return result

def selective_set(a, b):
  result = ""

  for i in range(len(a)):
    t = "1" if b[i] == "1" else a[i]
    result += t
  
  return result

while True:
  print ("===============MENU===============")
  print ("1. Selective Complement.")
  print ("2. Selective Clear.")
  print ("3. Selective Mask.")
  print ("4. Selective Set.")

  choice = int(input("Enter your choice: "))

  if choice == 1: 
    a = input("Enter first binary number : ")
    b = input("Enter second binary number : ")

    print ("Selective Complement = ", selective_complement(a, b))
  elif choice == 2:
    a = input("Enter first binary number : ")
    b = input("Enter second binary number : ")

    print ("Selective clear = ", selective_clear(a, b))
  elif choice == 3:
    a = input("Enter first binary number : ")
    b = input("Enter second binary number : ")

    print ("Selective Mask = ", selective_mask(a, b))
  elif choice == 4:
    a = input("Enter first binary number : ")
    b = input("Enter second binary number : ")

    print ("Selective Set = ", selective_set(a, b))
  elif choice == 5:
    break
  else:
    print ("Wrong choice... Try again!")
  


    
    
