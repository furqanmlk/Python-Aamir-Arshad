# Explain string data type in Python with examples.
# A string in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning once they are created, their content cannot be changed.    

# Example of creating strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, Python!"

triple_quote_string = '''Hello,
This is a multi-line string.''' 

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

# Accessing characters in a string
first_character = single_quote_string[0]  # 'H'
print("First character:", first_character)

last_character = single_quote_string[-1]  # '!'
print("Last character:", last_character)

# Slicing strings
substring = single_quote_string[0:5]  # 'Hello' i.e excluding index 5
substring = single_quote_string[:5]  # 'Hello' since starting index is 0 by default
print("Substring:", substring)
substring = single_quote_string[7:]  # 'World!' from index 7 to index end
print("Substring from index 7 to end:", substring)

substring = single_quote_string[7:10]  # 'Wor' from index 7 to index 10
print("Substring from index 7 to 10:", substring)

substring = single_quote_string[7:-3]  # 'Wor' from index 7 to index -3
print("Substring from index 7 to end:", substring)

# Specify step in slicing
str1 = "Hello!"
step_slice = str1[0:5:3]  # 'Hlo' from index 0 to 5 with step 2
print("Step slice:", step_slice)
