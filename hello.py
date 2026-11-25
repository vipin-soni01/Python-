print("Hello World")
print("From here the Python journey begins")
# input() - it is used to take input from the user

# input("What is ur name ? ")

name = input("What is ur name ?")
age = input("What is ur age? ")

print("Hi,"+ name)
print("Your age is:"+age)

print(name , age , sep=" ,U are a years old ") 


#  this is used to add something in the Quotes while writing a program. 
print("Hello , \"Friends\"")


print(f"Hello ,{name}") # this is now a froamted String or we can say special string 


# Remove the whitespace from the string from it's begining
name = name.strip()

name = name.capitalize()    #it will only capitalize the first alphabet of the string

print("Hello, ",name)

name = name.title() #it will capitalize the first alphabet of each letter in the string
print("Hii, ",name)



school = input("What is ur school name?").strip().title()
print("School Name: ",school)

first , last = school.split(" ")
print("First name:",first)
print("Last name:",last)