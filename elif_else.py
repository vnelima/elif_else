#2. Finding the Maximum of Three Numbers Using If-Elif-Else
##Problem Write a Python program that takes three numbers as input and
returns the largest of the three.
##Code Explanation
## Function to find the maximum of three numbers
def find_maximum(a, b, c):
if a >= b and a >= c: # Check if a is greater than or equal to both b and c
return a # If true, return a as the maximum
elif b >= a and b >= c: # Check if b is greater than or equal to both a and c
return b # If true, return b as the maximum
else:
return c # If neither a nor b are the maximum, return c
## Example usage
x = 10
y = 14
z = 12
max_value = find_maximum(x, y, z)
print(f"The maximum of {x}, {y}, and {z} is {max_value}.")
##Explanation for Presentation
###• Function Definition: def find_maximum(a, b, c): defines a function
to find the maximum of three numbers.
###• First Condition: if a >= b and a >= c: checks if a is greater than
or equal to both b and c. If true, a is returned as the maximum.
###• Second Condition: elif b >= a and b >= c: checks if b is greater
than or equal to both a and c. If true, b is returned as the maximum.
###• Else Condition: If neither of the above conditions is true, the function
returns c as the maximum.
###• Example Usage: The function is called with three values (x, y, z), and
the maximum value is printed.