# Create a program that reads a number and print their double, triple and square root.

number = int(input('Enter a number: '))
print('Double of {} is {}.\nTriple of {} is {}.\nSquare root of {} is {:.2f}.'.format(number, (number*2), number, (number * 3), number, (number ** (1/2))))
