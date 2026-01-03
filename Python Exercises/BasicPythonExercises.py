# 1. Formatted Twinkle Poem
# Write a Python program to print the following string in a specific format (see the output).
import sys
import datetime
print("\n")
print("Exercise#1: Formatted Twinkle Poem")
sample_String = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
print("""Twinkle, twinkle, little star, \n\tHow I wonder what you are!, \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are""")

# 2. Python Version Checker
# Write a Python program to get the Python version you are using.
print("\n")
print("Exercise#2: Python Version Checker")
print("Current Installed Python version is: " + sys.version)

# 3. Current DateTime Display
# Write a Python program to display the current date and time.
print("\n")
print("Exercise#3: Current DateTime Display")
current_DateTime = datetime.datetime.now()
print("Current Date and Time is: " +
      current_DateTime.strftime("%Y-%m-%d %H:%M:%S"))

# 4. Circle Area Calculator
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
print("\n")
print("Exercise#4: Circle Area Calculator")
radius = float(3.5)
area = 3.14 * radius**2
print("Area of the circle with given radius is:  " + str(area))

# 5. First and Last Name Input
# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
print("\n")
print("Exercise#5: First and Last Name Input")
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
print("Hello " + last_name + " " + first_name + "! Welcome aboard.")
