# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 9

def getChar():
    cha = input()
    if (cha == "<") or (cha == "+") or (cha == "&") or (cha == ">"):
        return cha
    else:
        print("You have entered an invalid operation.")
        print("Please try again:")
        cha = getChar()
    return cha
startStep = getChar()
dance = "<+&><+&>"
for i in range(4):
    if dance[i] != startStep:
        dance = dance + dance[i]
    else:
        print(dance[i::])


