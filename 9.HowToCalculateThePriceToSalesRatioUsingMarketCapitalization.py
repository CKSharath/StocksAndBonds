# Price to Sales (P/S) = MarketCap/Sales

#1.Stock X has a MarketCap of $500M and has a sales of $125M. What is its P/S?
def ptos(MarketCap,sales):
    return MarketCap/sales
print(f"\nX's P/S = {ptos(500,125)}")

#2.Stock ABC has a share price of $15 and 30M shares outstanding. It has $750M in annual sales.
#a)What is the market capitalization value
#b)What is the P/S ratio for this company?
def market_capitalization(share_out,market_price):
    return share_out*market_price
print(f"\nABC MarketCap {market_capitalization(30,15)}M")
print(f"\nABC's P/S = {ptos(market_capitalization(30,15),750)}")

#3.Stock GFK has a MarketCap of $2B and a P/S ratio of 0.25. Calculate the annual sales of this company.
print(f"\nGFK annual sales = {2/0.25}B")

#=> P/S ∝ 1/Sales 
