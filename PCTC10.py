# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 10

def getItems():
    x = input()
    return x

portion_I = 2
portion_W = 1
portion_M = 1
portion_C = 3

s = str(getItems())
if s.count("I") < portion_I:
    print("I")
elif s.count("W") < portion_W:
    print("W")
elif s.count("M") < portion_M:
    print("M")
elif s.count("C") < portion_C:
    print("C")


