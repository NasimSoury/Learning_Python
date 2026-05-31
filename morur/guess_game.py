

secret=7
while True:

    guess=int(input("add a number:"))
    if guess==secret:
        print("congratulations!you won!")
        break
    else:
        print("oh,sorry!try again!")
