# Create a program that read some input by keyboard and print in screen their primitive type and all possible information about it.

anything = input('Enter anything: ')
print('{} is their primitive type'.format(type(anything)))
print('Only spaces?', anything.isspace())
print('Is a number?', anything.isnumeric())
print('Is alphabetical?', anything.isalpha())
print('Is alphanumeric', anything.isalnum())
print('It\'s all in uppercase?', anything.isupper())
print('It\'s all in lowercase?', anything.islower())
print('It\'s titled?', anything.istitle())
