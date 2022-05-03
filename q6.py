# WAP to implement bitwise addition of two numbers

def if_binary(a):
  for x in a:
    if not int(x) in [0, 1]:
      return False
    
  return True

# def binary_addition(a, b):
#   i = len(a) - 1

#   carry = "0"

#   result = ""

#   while i >= 0:
#     sum = ""
#     carry = "0"

#     if a[i] == "1" and b[i] == "1":
#       sum = "0"
#       result = str(int(carry) + int(sum)) + result
#       carry = "1"
#     else:
#       sum = str(int(carry) + int(a[i]) + int(b[i]))
#       result = sum + result
    
#     i -= 1
  
#   if carry:
#     result = carry + result
  
#   return result

def binary_addition(a, b):
  result = ""
  temp = 0;
  a.size() - 1;
   int size_b = b.size() - 1;
   while (size_a >= 0 || size_b >= 0 || temp == 1){
      temp += ((size_a >= 0)? a[size_a] - '0': 0);
      temp += ((size_b >= 0)? b[size_b] - '0': 0);
      result = char(temp % 2 + '0') + result;
      temp /= 2;
      size_a--; size_b--;
   }
   return result;
}

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

if if_binary(a) and if_binary(b):
  print("Binary addition: ", binary_addition(a, b))
else:
  print ("Please provide binary numbers.")


