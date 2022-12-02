with open('input_puzzle1.txt') as f:
    lines = f.readlines()
    CalorieList = []
    amount = 0
    for i in lines:
        if i != '\n':
            amount += int(i)
        else:
            CalorieList.append(amount)
            amount = 0

    #answer puzzle 1 day 1
    print(max(CalorieList))
