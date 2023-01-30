# Perse Coding Team Challenge
# Round 1 Sample Paper
# Attempt by Mr Raymond Chng
# Question 8

def getNum():
    n = int(input())
    if (n < 1) or (n > 100):
        print("Your number has to be between 1 and 100 inclusive.")
        print("Please try again:")
        n = getFirstNum()
    return n

num = getNum()

print()
print("\./")
for i in range(num):
    print(".|.")

