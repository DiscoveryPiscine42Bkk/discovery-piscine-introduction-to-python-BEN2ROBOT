#!/usr/bin/env python
number01 = float(input("Enter the first number : ").strip()) 
number02 = float(input("Enter the second number : ").strip()) 
result = number01 * number02 
print (result)
if result > 0 :
    print("The result is positive.")
elif result < 0 :
    print("The result is negative.")
else : 
    print ("This result is  positive and negative.")
