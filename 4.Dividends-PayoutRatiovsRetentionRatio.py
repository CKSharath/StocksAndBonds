#payout ratio(PR) or dividend payout ratio(DPR) 
#PR=(total dividends paid by the company in a year)/(net income of the company)*100

#retention ratio(RR)=(retained earnings)/(net income)*100

# PR+RR=100%=1

def PR(total_dividend,net_income):
    if (total_dividend)/(net_income)*100>0:
        return (total_dividend)/(net_income)*100
    return 0
def RR(total_dividend,net_income):
    if (1-(PR(total_dividend,net_income)/100))*100>0:
        return (1-(PR(total_dividend,net_income)/100))*100
    return 0
    
#EG :       company A         company B         company C
#dividends    $20M              $40M              $150M
#net income   $100M             $100M             $100M
print(f"\nCompany A : PR : {PR(20,100)}% RR : {RR(20,100)}%")
print(f"\nCompany B : PR : {PR(40,100)}% RR : {RR(40,100)}%")
print(f"\nCompany C : PR : {PR(150,100)}% RR : {RR(150,100)}%") #one case where PR+RR!=1

#here company C is not retaining anything hence it's very bad
#here company B has good RR and PR
#company A has more RR which could be usually used to pay off dept or increase the operation which is also good
