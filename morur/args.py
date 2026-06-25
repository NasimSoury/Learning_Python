def zarb(*args):
    res=1
    for i in args:
        res=res*i
    return res

print(zarb(2,3,5))

