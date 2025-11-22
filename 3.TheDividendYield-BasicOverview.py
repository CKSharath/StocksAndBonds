#dividend yield
#how investers use dividend yield to know how much to invest in a stock
#Suppose a company ABC has dividend yield(DY)=5% it means if u invest $100 in it you'll get $5 annually if everything remains constant

#Formula of DY => DY=(annual dividend in $/stock price in $)*100
#DY ∝ annual dividend   DY ∝  1/stock price
#                       ^This is what says 'Buy low,sell high'


#1.Company XYZ pays an annual dividend of $1, Its current price is $20
#a)Calculate the dividend yield
#b)If the stock price increases to $50, what is the new dividend yield assuming the annual dividend remains constant
#c)What if the stock price drops to $10, what is the new dividend yield

def dividendYield(annualDividend,stockPrice):
    return annualDividend/stockPrice*100
print(f"\na) {dividendYield(1,20)}%")
print(f"\nb) {dividendYield(1,50)}%")
print(f"\nc) {dividendYield(1,10)}%")


#2.Company ABC pays a quarterly dividend of $0.5. It's current stock price is $50
#a)What is the dividend yield of this company?
#b)If an investor buys $10000 worth of stock, how much money does he expect to earn annually in annually in dividends
#assuming the stock price and annual dividend remains constant
quarterly_dividend=0.5
annual_dividend=quarterly_dividend*4
current_stock_price=50
invest=10000
print(f"\na) {dividendYield(annual_dividend,current_stock_price)}%")
print(f"\nb) {invest*dividendYield(annual_dividend,current_stock_price)/100}$")
