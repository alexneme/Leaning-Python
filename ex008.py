# Create a program that reads a number value in meters and print that converted by centimeters and millimeters.

m = float(input('Enter number is meters: '))
print('{:.1f}m in centimeters = {:.1f}cm.'.format(m, m*100))
print('{:.1f}m in millimeters = {:.1f}mm.'.format(m, m*1000))
