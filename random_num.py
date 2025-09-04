from random import randint
answer= randint(1,6)

i=input("wich number did you take : ")
i=int(i)

if i==answer :
    print("wowww! you was correct!")
else:
    print(f"no! for me was {answer}! ")

