dict = {  "Rock": ["A", "X"],
  "Paper": ["B", "Y"],
  "Scissors": ["C", "Z"]
}
score = 0
opponent = ""
result = ""
with open('D:\Github\AdventOfCode\AOC day 2\input_puzzle2.txt') as f:
    lines = f.readlines()

    for i in lines:

        #spilts up string into dict values
        result = i.split(" ")[1].replace("\n", "")
        opponent_1 = i.split(" ")[0]

        #checks what value the opponent has (Rock, Paper or Scissors)
        for key, val in dict.items():
            for x in val:
                if x == opponent_1:
                    opponent = key

        #if stateresultnt only for draw and then win because lose is 0 points so no need to check
        # draw
        if result == "Y":
            score += (3 + (list(dict).index(opponent) +1))

        # Win
        elif result == "Z":
            if opponent == "Scissors":
                score += 7
            if opponent == "Rock":
                score += 8
            if opponent == "Paper":
                score += 9
        # Lose
        elif result == "X":
            if opponent == "Scissors":
                score += 2
            if opponent == "Rock":
                score += 3
            if opponent == "Paper":
                score += 1

    print(score)
