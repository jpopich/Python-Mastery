#.title(), .upper(), .lower(), \n, \t, rstrip()
name = "ada lovelace"
print(name.title())
print("\n")

print(name.upper())
print(name.lower())
print("\n")

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("\n")

print("Hello, " + full_name.title() + "!")
print("\n")

message = "Hello, " + full_name.upper() + "!"
print(message)
print("\n")

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("\n")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print("\n")

favorite_language = 'python    '
print(favorite_language.rstrip())
print(favorite_language)
print("\n")

favorite_language = "  python  "
print("." + favorite_language.rstrip() + ".")
print("." + favorite_language.lstrip() + ".")
print("." + favorite_language.strip() + ".")
print("\n")

# Showing error with single quotes around a string that has an apostrophe in string
# newMessage = 'One of Python's strengths is its diverse community.'
print("\n")

print("Hello Python 2.7 world!")











