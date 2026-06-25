def sum_numbers(*args):
    print(args)
    if len(args)==0:
        return 0
    return sum(args)

print(sum_numbers(2,5,4,1))