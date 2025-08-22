def average(scores):
    total=sum(scores) / len(scores)
    return total

    if total <10:
        print("failed")
    elif total<15:
        print("normal")  
    else:
        print("passed")

print(average([12,18,19,20]))