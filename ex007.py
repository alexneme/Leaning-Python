# Create a program that reads two grades, calculate and print their avarege.

grade1 = float(input('Enter your first grade: '))
grade2 = float(input('Enter your second grade: '))
print('Avarege between {:.2f} and {:.2f} is: {:.2f}.'.format(grade1, grade2, (grade1+grade2)/2))
