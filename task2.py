def find(stock):
    file = 'task02.csv'
    file = open(file, 'r')
    list = []
    count = 0
    for i in file:
        if stock in i:
            count = count + 1
            test = i.strip()
            Data = test.split(",")
            
            list.append(Data[1])
    
    if len(list) > 1:
        print(f"There is {len(list)} stocks with that symbol")
    elif len(list) == 0:
        print("No matches")