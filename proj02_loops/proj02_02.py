# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

pn = 0
cn = 1
nn = 1


x = int(raw_input("Enter a number:"))
for f in range(1,x):
    print cn
    pn = cn
    cn = nn
    nn = cn + pn

pn = 1
cn = 2
nn = 4

# Powers of 2 Extensions

x = int(raw_input("Enter a number:"))
for f in range(1,x):
    print cn
    pn = cn
    cn = nn
    nn = cn + pn






x = int(raw_input("Enter a number:"))
for f in range(1,x):
    if x%f == 0:
        print f

