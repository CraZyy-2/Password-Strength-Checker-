import string

print("WELCOME")
print("Check the strength of your password using this simple tool")

score = 0



password = input("Input your password :  ")


upper = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])


characters = [upper, lower, special, digits]

with open('10 million psswd.txt', 'r') as f:
    common = f.read().splitlines()
if password in common :
    print("This password has been found in a long list of weak and commonly used passwords. Score : 0/8")
    exit()
else : score += 1

length = len(password)
if length > 8:
    score += 1
if length > 12 :
    score += 1
if length > 18 :
    score += 1
if length > 25 :
    score += 1


print (f"Your password's length is {str(length)}, adding {str(score)} point.")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3 :
    score += 1

print (f"Your password has {str(sum(characters))} types of characters, and your total score is {(str(score))} out of 8")

if score < 4 :
    print("This password is very weak, it would be recommended not to use it")
elif score == 4 :
    print("This password is decent, it is recommended to complicate it even more")
elif score > 4 and score < 6:
    print("This password is good, but still could be better")
elif score > 6 :
    print("This password is great, you should use it for sure")