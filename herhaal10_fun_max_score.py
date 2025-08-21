def find_max_score(scores):
    max_score=scores[0]
# eshtebah neveshte boodam: for s in range(scores):
    for s in scores:
        if s>max_score:
            max_score=s    #eshtebah nev boodam: max_score == s ama 2 ta mosavi baraye moghayese hast!
    return max_score


print(find_max_score([3,12,16,14,11]))