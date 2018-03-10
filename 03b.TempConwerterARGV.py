import sys
from sys import argv

number = float(sys.argv[1])
c_or_f = sys.argv[2]

if c_or_f == "-c":
    celsius_to_farenheit = (number * 1.8) + 32
    print("Your value in Farenheit is: %.2f" % celsius_to_farenheit)
elif c_or_f == "-f":
    farenheit_to_celsius = (number - 32) / 1.8
    print("Your value in Celsius is: %.2f" % farenheit_to_celsius)
else:
    print("Incorrect format")
