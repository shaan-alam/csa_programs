def binary_list(nibble):
  if nibble<=1111 and nibble>=0000:
    i=k=0
    for i in range(0,4,1):
      k=nibble%10
      nibble/=10
      k=int(k)
      if k==1 or k==0:
        result.insert(0,k)
      else:
        print(k," is non binary number")
        return -1
  return 0

# count_down
def count_down():
  for i in range(1,5,1):
    k=result[-i]
    if result[-i]==0:
      result[-i]=1
    else:
      result[-i]=0
    if k==1:
      return 0
  return 0

# count up
def count_up():
  for i in range(1,5,1):
    k=result[-i]
    if result[-i]==0:
      result[-i]=1
    else:
      result[-i]=0
    if k==0:
      return 0
  return 0

def main():
  global result
  result=[]
  nibble=int(input("Enter 4 digit binary number: "))
  binary_list(nibble)
  count=int(input("Enter 0 for count down and 1 for count up : "))
  if count==0:
    print("Count up:\n")
    for i in range(0,16,1):
      count_down()
      print(*result)
  elif count==1:
    print("Count up:\n")
    for i in range(0,16,1):
      count_up()
      print(*result)
  else:
    print("Wrong input")
    return -1
  
  return 0
run=main()