# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 3

def getWord():
    w = str(input())
    if w.isalpha() and w.islower():
        if len(w) < 50:
            return w
        else:
            print("Your word has to be less than 50 characters.")
            print("Please try again:")
            w = getWord()
    else:
        print("Your word can only consist of lowercase characters.")
        print("Please try again:")
        w = getWord()
    return w

word = str(getWord())
result = word
for i in range(30 // len(word)):
    result = result + word
print(result)
