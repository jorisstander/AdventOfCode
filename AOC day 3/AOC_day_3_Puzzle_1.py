import string

with open('D:\Github\AdventOfCode\AOC day 3\input_puzzle3.txt') as f:
    lines = f.readlines()
    endScores = []
    points = string.ascii_lowercase + string.ascii_uppercase
    for i in lines:
        i = i.replace("\n", "")
        left = i[:len(i)//2]
        right = i[len(i)//2:]
        score = 0 
        list = [] 

        #a is first value in left
        for a in left:
            #b is first value in right
            for b in right:
                # check if values are the same
                if a == b:
                    #check if value isnt in list already
                    if a not in list:

                        #append value since its not in the list and calculate score
                        list.append(a)
                        score += (points.index(a) +1)

        # add endscore to list so i can sum up later        
        endScores.append(score) 
    print(sum(endScores))

    

           

