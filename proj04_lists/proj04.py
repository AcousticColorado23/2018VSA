# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

for item in a:
    if item <= 5:
        print item





#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


for item in b:
    for item_c in c:
        if item == item_c:
            print item




#Part III
# Take a list, say for example this one:
# and write a program that replaces all “a” with “*”.

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
on = ("a")
nn = ("*")
counter = 0

for item in d:
    if d[counter] == on:
        d[counter] = nn
    counter = counter + 1
print d


#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

l2 = []
l = []
song = raw_input("Please enter a word. ")

for letter in song:
    l.append(letter)
    l2.append(letter)
print l
l2.reverse()
print l2
l3 = []

l = []
song = raw_input("Please enter a word. ")
for letter in song:
    l.append(letter)
    l2.append(letter)
print l
for num in range(0, len(song)):
    let = len(song) - num -1
    l3.append(l[let])          
print l3






