# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 2

def getFirstNum():
    num1 = int(input())
    if (num1 < 0) or (num1 > 1000):
        print("Your number has to be between 0 and 1000 inclusive.")
        print("Please try again:")
        num1 = getFirstNum()
    return num1

def getSecondNum():
    num2 = int(input())
    if (num2 < 0) or (num2 > 1000):
        print("Your number has to be between 0 and 1000 inclusive.")
        print("Please try again:")
        num2 = getSecondNum()
    return num2

def compareNums():
    num1 = getFirstNum()
    num2 = getSecondNum()
    while num1 == num2:
        print("This number is already in use.")
        print("Please try again:")
        num2 = getSecondNum()
    if num1 > num2:
        return num1 - num2
    elif num1 < num2:
        return num2 - num1

print(compareNums())
