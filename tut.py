# SNAKE WATER GUN
import random
items = ["snake","water","gun"]

user = 0
computer = 0
print("U are about to play snake water gun with the computer \n")
n = int(input("Enter the number of rounds u want to play: "))
for i in range(0,n):
    d = input("enter your choice :")
    comp2 = random.choice(items)
    if d == "snake" and comp2 != "snake":
        if comp2 == "water":
            user +=1
        else:
            computer += 1
        print("computer chose: ", comp2)
        print("CURRENT SCORE: \n user:",user,"\n computer:",computer)
    if d == "water" and comp2 != 'water':
        if comp2 == "snake":
            computer += 1
        elif comp2 == "gun":
            user += 1
        print("computer chose: ", comp2)
        print("CURRENT SCORE: \n user:",user,"\n computer:",computer)
    if d=="gun" and comp2 != "gun":
        if comp2 == "snake":
            user +=1
        else:
            computer +=1
        print("computer chose: ", comp2)
        print("CURRENT SCORE: \n user:",user,"\n computer:",computer)
    if d == comp2:
        user += 0
        computer += 0
        print("computer chose: ", comp2)
        print("CURRENT SCORE: \n user",user,"\n computer:",computer,"\n")
# print(" FINAL SCORE : ", user, computer)
print("FINAL SCORE: \n user:",user,"\n computer:",computer)
