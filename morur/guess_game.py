

secret=6
for i in range(3):

    guess=int(input("add a number:"))
    if guess==secret:
        print("congratulations!you won!")
        break
    else:
        print("oh,sorry!try again!")
else:
    print("game over!")