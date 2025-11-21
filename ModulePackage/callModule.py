
# # Approach 1
# import mod1
# mod1.printName('Furqan Malik')
# mod1.printAge(30)

# # Approach 2
# from mod1 import printName, printAge
# printName('Aamir Arshad')
# printAge(25)

# # Approach 3
# from mod1 import *
# printName('John Doe')
# printAge(40)


# Approach 4: Demonstrating naming conflict
from mod1 import printName
from mod2 import printName
printName('Furqan Malik')   # This will call printName from mod2 due to the last import

# Approach 5: Using module names to avoid conflict
import mod1
import mod2
mod1.printName('Furqan Malik')
mod2.printName('Aamir Arshad')

# Approach 6: Calling  specific functions right after import
from mod1 import printName
printName('Alice')  # Calls printName from mod1

from mod2 import printName
printName('Bob')    # Calls printName from mod2