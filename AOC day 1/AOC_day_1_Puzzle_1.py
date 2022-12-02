with open('input_puzzle1.txt') as f:
    lines = f.readlines()
    CalorieList = []
    amount = 0
    counterIndex = 0
    for i in lines:
        if i != '\n':
            amount += int(i)
        else:
            counterIndex += 1
            CalorieList.append(amount)
            amount = 0
    
    print(max(CalorieList))
