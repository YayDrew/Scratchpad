print("There is power here unmeasured!")

#Variables store data in memory. Strings, numbers, booleans, etc.
name = "Andrew"
age = 63

#Printing + f-strings   f"{} lets you embed variables right in strings.
print(f"{name} is {age} years old.")

#Functions are reusable chunks of code. Great for breaking problems down.
def greet(person):
    print(f"Hello, {person}!")

greet(name)

#If statements for logic and branching.
if age > 50:
    print("You're really old.")

else:
    print("You ain't seen nothing yet!")

#Lists (Arrays) /lists store ordered data. Indexed from 0.
colours = ["red", "blue", "green"]
print(colours[1]) #prints "blue"

#Loops repeat actions -- great with lists, files, etc.
for colour in colours:
    print(colour)

#User Input
favourite_colour = input("What is your favourite colour? ")
print(f"Ah, {favourite_colour} - Really? Well, to each their own!")

#Simple Arithmetic
birth_year = 1961
current_year = 2025
calculated_age = current_year - birth_year
print(f"You're {calculated_age} (plus or minus) years old.")

#A Function that loops
def list_colours(colour_list):
    print("Here are some colours:")
    for c in colour_list:
        print(f" - {c}")

list_colours(colours)