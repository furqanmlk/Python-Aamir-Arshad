# I want to create some number variables with some arithmetic operations
x = 5
y = 2

print(x+y)  # Output: 7

print(x*y)  # Output: 10  

print(x/y)  # Output: 2.5  

# Exponentiation
print(x**3)  # x=5, y=3 5*5*5 Output: 125

print(x//y)  # Output: 2

print(x%y)  # Output: 1  # Modulus operator gives the remainder

# Find if a number is even or odd
l1= [1,2,3,4,5]
for num in l1:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Convert number to string
num = 100
print(type(num))  # Output: <class 'int'>

num_str = str(num)
print(type(num_str))  # Output: <class 'str'>

# Convert string to number
num2_str = "200"
num2 = int(num2_str)
print(type(num2))  # Output: <class 'int'>



