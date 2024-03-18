# Python String Methods Practice
# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
capitalize_string1 = string1.capitalize()
print(string1.capitalize())

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> " python "
string2 = "python"
center_string2 = string2.center(5)
print(string2.center(5))

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
endswithon = string3.endswith("on")
print(string3.endswith("on"))

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
position_of_th = string4.find("th")
print(string4.find("th"))

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
alphanumeric = string5.isalnum()
print(string5.isalnum())

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
alpha = string6.isalpha()
print(string6.isalpha())

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
lowercase = string7.islower()
print(string7.islower())

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if " " is all whitespace
string8 = " "
space = string8.isspace()
print(string8.isspace())

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
uppercase = string9.isupper()
print(string9.isupper())

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
joined_string = separator.join(iterable1)
print(separator.join(iterable1))

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
lowercase_string10 = string10.lower()
print(string10.lower())

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from " python"
string11 = " python"
stripped_string11 = string11.lstrip()
print(string11.lstrip())

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python "
string12 = "python "
stripped_string12 = string12.rstrip()
print(string12.rstrip())

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
replaced_string13 = string13.replace("python", "snake")
print(string13.replace("python", "snake"))

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
highest_index = string14.rfind("n")
print(string14.rfind("n"))

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
split_string15 = string15.split("-")
print(string15.split("-"))

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
starts_with_py = string16.startswith("py")
print(string16.startswith("py"))

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from " python "
string17 = " python "
stripped_string17 = string17.strip()
print(string17.strip())

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
swapped_case_string18 = string18.swapcase()
print(string18.swapcase())

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
title_case_string19 = string19.title()
print(string19.title())

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
uppercase_string20 = string20.upper()
print(string20.upper())