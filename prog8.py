
a = eval(input("Enter a: "))
b = eval(input("Enter b: ")) 

print ("\nResults : ", end = "\n\n")

# Print bitwise AND operation
print(a, " & ", b, " = ", (a & b))
 
# Print bitwise OR operation
print(a, " | ", b, " = ", (a | b))
 
# Print bitwise NOT operation
print("~a =", ~a)
print("~b =", ~b)

# print bitwise XOR operation
print(a, " ^ ", b, " = ", (a ^ b))