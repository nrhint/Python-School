##Nathan Hinton

##Inputs:
#Types of coins
#Total number of coins
#Value of coins

##Run:

coins = []
i = True
print("MAXIUM OF 2 COINS!")
while i == True:
    inp = input(
        """q = quit
1 = Pennies
5 = Nickles
10 = Dimes
25 = Quarters
""")
    if inp == 'q':
        i = False
    else:
        coins.append(int(inp))

print()    
totalNumber = -int(input("total number of coins: "))
totalValue = int(input("Total value: "))

coins.sort()
value = totalValue+(totalNumber*coins[0])
number = coins[1]-coins[0]

largerCoin = value/number
smallerCoin = -totalNumber-largerCoin

print("Larger coin %s"%largerCoin)
print("Smaller coin %s"%smallerCoin)
