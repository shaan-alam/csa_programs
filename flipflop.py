
def srflipflop(a, b, Q):
  if not(s) and not(r):
    print ("No Change")
    return 1 if Q else 0
  elif not(s) and r:
    print ("Reset")
  elif s and not(r):
    print ("Set")
    return ''
  else:
    print ("Invalid")
    return ''

def jkflipflop(j, k , Q):
  if not(j) and not(k):
    print ("No Change")
  elif not(j) and k:
    print ("Reset")
    return 0
  elif j and not(k):
    print ("Set")
    return 1
  else:
    print ("Complement")
    return 0 if Q else 1

def dflipflop(d):
    if(d == 0):
      print("Reset")
    elif(d == 1):
      print("Set")
    else:
      print ("Invalid Input")
      return ''

def tflipflop(t):
  if(t == 0):
    print("Toggle")
  elif(t == 1):
    print("Hold")
  else:
    print ("Invalid Input")

print ("===========MENU===========")
print ("SR Flip Flop")
print ("JK Flip Flop")
print ("D Flip Flop")
print ("T Flip Flop")

choice = int(input("Enter your choice: "))

if choice == 1:
  s = int(input("Enter s value: "))
  r = int(input("Enter r value: "))

  srflipflop(s, r, 1)
elif choice == 2:
  j = int(input("Enter s value: "))
  k = int(input("Enter r value: "))

  jkflipflop(j, k, 1)
elif choice == 3:
  d = int(input("Enter d value: "))

  dflipflop(d)
elif choice == 4:
  t = int(input("Enter t value: "))

  tflipflop(t)
else:
  print ("Wrong choice!!")

