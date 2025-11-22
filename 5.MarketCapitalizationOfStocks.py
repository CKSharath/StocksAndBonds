#Market Capitalization = (Shares outstanding)*(market price)

#Shares outstanding refer to the total number of shares of a company's stock that are currently held by all its shareholders, 
#including institutional investors, company insiders, and the general public

#1.Company XYZ has 42M shares outstanding and a market price of $24.50 per share. WHat is the market capitalization of company XYZ

#MC= x (shares)* price ($/shares) => unit is $

def market_capitalization(share_out,market_price):
    return share_out*market_price
print(f"\nMarket capitalization of XYZ is {market_capitalization(42000000,24.50)}$")

#2.Company ABC has 50M shares in float and 30M restricted shares. If a stock of company ABC is selling for $45 on the open market_capitalization
#what is the market capitalization of company ABC

share_out_ABC=50+30
print(f"\nMarket capitalization of ABC is {market_capitalization(share_out_ABC*1000000,45)}$")
