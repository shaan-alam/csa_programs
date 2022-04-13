def binary_list(byte):
  if byte<=11111111 and byte>=00000000:
    i=k=0
    for i in range(0,8,1):
      k=byte%10
      byte/=10
      k=int(k)
      if k==1 or k==0:
        result.insert(0,k)
  return result

def one(listem):
  for i in range(0,8,1):
    if listem[i]==0:
      listem[i]=1
    else:
      listem[i]=0
  return listem

def two(listem):
  listem=one(listem)
  for i in range(1,9,1):
    k=listem[-i]
    if listem[-i]==0:
      listem[-i]=1
    else:
      listem[-i]=0
    if k==0:
      return listem
  return listem

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
  result1=[]
  result2=[]
  result2c=[]
  resultadd=[]
  byte1=int(input("Enter 8 digit binary number 1: "))
  result1=binary_list(byte1)
  result=[]
  byte2=int(input("Enter 8 digit binary number 2: "))
  result2=binary_list(byte2)
  if byte1>=byte2:
    result2c=two(result2)
    resultadd=add(result1,result2c)
    print("Result Number 1 - Number2: ", *resultadd)
  else:
    result2c=two(result1)
    resultadd=add(result2,result2c)
    print("Result Number 2 - Number 1: ", *resultadd)

  return 0
run=main()