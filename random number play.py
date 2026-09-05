import random
num = random.randint(0, 10)
quest = int(input("gave an number between 1 to 10:"))
while quest != num:
    quest = int(input("try agan! : "))
else:
    print("done, you are correct!")
