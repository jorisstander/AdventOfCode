dict = {  "Rock": ["A", "X"],
  "Paper": ["B", "Y"],
  "Scissors": ["C", "Z"]
}
score = 0
opponent = ""
me = ""
with open('D:\Github\AdventOfCode\AOC day 2\input_puzzle2.txt') as f:
    lines = f.readlines()

    for i in lines:

        #spilts up string into dict values
        me_1 = i.split(" ")[1].replace("\n", "")
        opponent_1 = i.split(" ")[0]

        #checks what value is Rock, Paper or Scissors and saves it to detemine match up
        for key, val in dict.items():
            for x in val:
                if x == me_1:
                    me = key
                if x == opponent_1:
                    opponent = key
        
        #print("the Match is: %s (me) vs %s (opponent)" %(me, opponent))

        # counts the score for picking a certain hand (index +1 in dict)
        score += (list(dict).index(me) +1)

        #if statement only for draw and then win because lose is 0 points so no need to check
        if me == opponent:
            score += 3
        elif me == "Rock":
            if opponent == "Scissors":
                score += 6
        elif me == "Paper":
            if opponent == "Rock":
                score += 6
        elif me == "Scissors":
            if opponent == "Paper":
                score += 6
    print(score)
            