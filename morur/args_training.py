def pick_evens(*args):
    print(args)
    evens=[]
    for i in args:
        if i%2==0:
            evens.append(i)
    return evens



print(pick_evens(1,2,3,4,5,6,7,8,10))