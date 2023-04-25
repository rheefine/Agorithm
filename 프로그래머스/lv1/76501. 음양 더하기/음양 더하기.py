def solution(absolutes, signs):
    numlist = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            numlist.append(absolutes[i])
        else:
            numlist.append(-absolutes[i])
    answer = sum(numlist)
    return answer