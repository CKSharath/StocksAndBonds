# Earnings Per Share (EPS) =Earnings/SharesOut if the company does't give any dividends
# if it does          EPS=((Net income)-(preferred dividends))/SharesOut

#Eg:        company A           company B
#Earnings     $100M               $100M
#SharesOut    10M                 50M
#ESP          $10/share           $2/share 

#company A is a better deal since EPS is higher than B

# High EPS => Good
# Low EPS => Bad
#EPS(A) = +5.6  eps is +ve then company A is good and making money
#EPS(B) = -3.8  eps is +ve then company B is bad and losing money

#Price to Earnings (P/E)

# P     MarketCap   Shares*Price    Price
# -- =  --------- = ------------ =  ------
# E     Earnings    Shares*EPS      EPS

#Eg:            Company A       Company B
#Share price      $40             $40
#EPS              $10             $5
#P/E=>            $4              $8
#hence      A is undervalued    B is overvalued

#1.A company has $450M in earnings and 300M shares outstanding. The current price of the stock is $30.
#a)What is the EPS value of this company?
#b)Calculate P/E ratio
def eps(Net_income,SharesOut,preferred_dividends=0):
    return ((Net_income)-(preferred_dividends))/SharesOut
def PEr(price,epsv):
    return price/epsv
print(f"\n1. EPS of company A is {eps(450,300)}")
print(f"\n2. P/E of company A is {PEr(30,eps(450,300))}")

#2.Company X has $4.2B in net income and $300M that is must pay out in preferred dividends. The company has 900M SharesOut
#and is trading at a stock price of $45
#a)Calculate the EPS 
#b)P/E =?

print(f"\n1. EPS of company X is {eps(4.2*1000,900,300)}")
print(f"\n2. P/E of company X is {PEr(45,eps(4.2*1000,900,300))}")

#3.Company ABC has a MarketCap of $2.8B and has $400M in earnings. (No preferred_dividends) The stock is currently trading at
#$35
#a)What is the P/E ratio for this company
#b)Calculate EPS
#c)Estimate number of SharesOut
print(f"\n2. EPS of company ABC is {eps(400,2800/35)}")
print(f"\n1. P/E of company ABC is {PEr(35,eps(400,2800/35))}")
print(f"\n3. SharesOut=MarketCap/(share price) of company ABC is {2800000000/35}")
