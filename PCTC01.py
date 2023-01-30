# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 1

def getGreeting():
    greeting = input()
    if len(greeting) > 20:
        print("Your greeting has to be less than 20 characters long.")
        print("Please try again:")
        greeting = getGreeting()
    return greeting

def getName():
    name = input()
    if len(name) > 20:
        print("Your name has to be less than 20 characters long.")
        print("Please try again:")
        name = getName()
    return name

print(getGreeting() , getName())
