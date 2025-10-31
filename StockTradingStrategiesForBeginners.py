def sell(person,shares,oldprice,newprice):
    if info[person]['shares']-shares<0:
        print(f"{person} tried to sell {shares} amount of shares but had only {info[person]['shares']} shares so trade has been cancelled.")
        return 0
    info[person]['profit']+=(shares*(newprice-oldprice))
    info[person]['shares']-=shares

def printProfit(info):
    print("--"*15)
    for n,p in info.items():
        print(f"{n} made this trade {p['profit']}$")
    print("--"*15)

def buy(person,shares,price):
    info[person]['profit']-=(shares*price)
    info[person]['shares']+=shares
##################################################################################################################################################

# Jhon, Kelly and Bruce but 1000 shares of stock XYZ which is trading at $10. The stock goes
# up to $20 in 1 month. Jhon sells all of his shares at this price. Kelly decides to hold
# on to her investment. Bruce sells 500 of his shares. The stock goes up to $40 in the next 
# month. Kelly sells her entire investment and Bruce sells the remaining 500 shares.
# Which individual generated the most profit?

# 10->20->40

info = {
    'Jhon': {'shares': 1000, 'profit': 0},
    'Kelly': {'shares': 1000, 'profit': 0},
    'Bruce': {'shares': 1000, 'profit': 0}
}
sell('Jhon',1000,10,20)
sell('Bruce',500,10,20)
sell('Kelly',1000,10,40)
sell('Bruce',500,10,40)
printProfit(info)

##################################################################################################################################################

# Jhon, Kelly and Bruce but 1000 shares of stock XYZ which is trading at $10. The stock goes
# up to $20 in 1 month. Jhon sells all of his shares at this price. Kelly decides to hold
# on to her investment. Bruce sells 500 of his shares. The stock goes down to $5 in the next 
# month. Kelly sells her entire investment and Bruce sells the remaining 500 shares.
# Which individual generated the most profit?

# 10->20->5

info = {
    'Jhon': {'shares': 1000, 'profit': 0},
    'Kelly': {'shares': 1000, 'profit': 0},
    'Bruce': {'shares': 1000, 'profit': 0}
}
sell('Jhon',1000,10,20)
sell('Bruce',500,10,20)
sell('Kelly',1000,10,5)
sell('Bruce',500,10,5)
printProfit(info)

##################################################################################################################################################

# Another case where Bruce but 1000 shares of stock XYZ which is trading at $10. The stock goes
# up to $20 in 1 month.  Bruce sells 500 of his shares. The stock goes down to $5 in the next 
# month. He buys that shares with all of his profit . The stock goes up again to $20
# How much profit did he make?

# 10->20->5->20
info = {
    'Jhon': {'shares': 1000, 'profit': 0},
    'Kelly': {'shares': 1000, 'profit': 0},
    'Bruce': {'shares': 1000, 'profit': 0}
}
sell('Bruce',500,10,20)
sh=info['Bruce']['profit']//5
buy('Bruce',sh,5)
sell('Bruce',500,10,20)
sell('Bruce',sh,5,20)
printProfit(info)

