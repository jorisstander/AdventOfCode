import string

#compares
def group_check(group):
    for a in group[0]:
        if a in group[1]:
            if a in group[2]:
                return a

with open('D:\Github\AdventOfCode\AOC day 3\input_puzzle3.txt') as f:
    lines = f.readlines()
    endScores = []
    points = string.ascii_lowercase + string.ascii_uppercase

    groupmembercount = 0
    group = []

    for i in lines:
        #create a group of 3 and remove the enter from the string
        i = i.replace("\n", "")
        group.append(i)
        groupmembercount += 1

        #start the comparing part
        if groupmembercount == 3:
            endScores.append(points.index(group_check(group)) +1)

            #reset values
            groupmembercount = 0
            group = []
    
    print(sum(endScores))

