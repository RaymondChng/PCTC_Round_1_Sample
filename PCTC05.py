# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 5

def getFirstNum():
    num1 = int(input())
    if (num1 < -100) or (num1 > 100):
        print("Your number has to be between -100 and 100.")
        print("Please try again:")
        num1 = getFirstNum()
    return num1

def getSecondNum():
    num2 = int(input())
    if (num2 < -100) or (num2 > 100):
        print("Your number has to be between -100 and 100.")
        print("Please try again:")
        num2 = getSecondNum()
    return num2

def getOperator():
    op = input()
    if (op == "*") or (op == "+"):
        return op
    else:
        print("You have entered an invalid operation.")
        print("Please try again:")
        op = getOperator()

num1 = int(getFirstNum())
op = str(getOperator())
num2 = int(getSecondNum())

if op == "*":
    print(num1 * num2)
else:
    print(num1 + num2)
