import re
with open('D:\Github\AdventOfCode\AOC day 4\input_puzzle4.txt') as f:
    lines = f.readlines()
    score = 0
    for i in lines:
        
        list = re.split('-|,',i.replace("\n",""))
        
        print(list)
        if int(list[2]) >= int(list[0]) and int(list[2]) <= int(list[1]):
                score += 1
        elif int(list[3]) >= int(list[0]) and int(list[2]) <= int(list[1]):
                score += 1

    print(score)