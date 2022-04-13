def binary_list(byte,bit):
  if byte<=11111111 and byte>=00000000:
    i=k=0
    for i in range(0,8,1):
      k=byte%10
      byte/=10
      k=int(k)
      if k==1 or k==0:
        result.insert(0,k)
  if bit==0:
    global result0
    result0=result
  return 0

def add(result1,result2c):
  templist=[]
  carry=0
  for i in range(-1,-9,-1):
    if result1[i]==0 and result2c[i]==0 and carry==0:
      carry=0
      templist.insert(0,0)
    elif result1[i]==0 and result2c[i]==0 and carry==1:
      carry=0
      templist.insert(0,1)
    elif result1[i]==0 and result2c[i]==1 and carry==0:
      carry=0
      templist.insert(0,1)
    elif result1[i]==0 and result2c[i]==1 and carry==1:
      carry=1
      templist.insert(0,0)
    elif result1[i]==1 and result2c[i]==0 and carry==0:
      carry=0
      templist.insert(0,1)
    elif result1[i]==1 and result2c[i]==0 and carry==1:
      carry=1
      templist.insert(0,0)
    elif result1[i]==1 and result2c[i]==1 and carry==0:
      carry=1
      templist.insert(0,0)
    elif result1[i]==1 and result2c[i]==1 and carry==1:
      carry=1
      templist.insert(0,1)
  return templist

def main():
  global result
  result=[]
  byte=int(input("Enter 8 digit binary number: "))
  binary_list(byte,0)
  result=[]
  byte2=int(input("Enter 8 digit binary number: "))
  binary_list(byte2,1)

  added=add(result0,result)
  print("bitwise addition of ",byte," and ",byte2," is ", *added,sep="")
  
  return 0
run=main()