# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

print " Sup dude"
name = raw_input ("What is your name")
grad_year = raw_input ("What grade are you in?")
print name + " you graduate in " + str(12-int(grad_year)) + " years."

print "Hi"
name = raw_input ("What is your name?")
name = name[0].upper() + name[1:100].lower()
print name



# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

print"hi"
month = int(raw_input("What is your birth month (number)?"))
day = int(raw_input("What is your birthday (number)?"))
cm = int(raw_input("What is the current month (number)?"))
cd = int(raw_input("What is you current day (number)?"))
if month >= cm:
    print "Your birthday is in " + str(month - cm) + " months!"
elif cm >= month:
    print "Your birthday is in " + str(12-(cm - month)) + " months!"
if day >= cd:
    print "Your birthday is in " + str(day - cd)  + " days!"
elif cd >= day:
    print "Your birthday is in " + str(30 -(cd - day)) + " days!"

    





# If you complete extensions, describe your extensions here!