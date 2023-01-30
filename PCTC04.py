# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 4

def getNum():
    num = int(input())
    if (num < 1) or (num > 100):
        print("Your number has to be between 1 and 100 inclusive.")
        print("Please try again:")
        num = getNum()
    return num

numberChoice = int(getNum())
if numberChoice > 50:
    print("yes dream big")
else:
    print("on the small side")

