
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
    D = int(input("Enter the value of D "))

    if(D == 0):
      print("Reset")
    elif(D == 1):
      print("Set")

def tflipflop():
  T = int(input("Enter the value of T "))
  if(T == 0):
    print("Set")
  elif(T == 1):
    print("Reset")

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
  d = int(input("Enter s value: "))

  dflipflop(d)
elif choice == 4:
  t = int(input("Enter r value: "))

  tflipflop(t)
else:
  print ("Wrong choice!!")

