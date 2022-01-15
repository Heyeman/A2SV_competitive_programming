# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, atan
a = int(input())
b = int(input())
print(str(round(degrees(atan(a/b)))) + u"\N{DEGREE SIGN}")
