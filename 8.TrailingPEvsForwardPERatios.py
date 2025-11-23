def PEr(price,epsv):
    return price/epsv
#1.The earnings per share (ttm) company X is $4.25 and next year's estimated eps value is %5.00. The current share price
#of company X is $34.
#a)What is the trailing P/E ratio?(Past)
#b)Calculate the forward P/E ratio(Future)          #ttm->trailing twelve months

#trailing P/E=price/EPS(ttm)
print(f"\nTrailing P/E ratio = {PEr(34,4.25)}")
print(f"\nForward P/E ratio = {PEr(34,5)}")

#2.Stock ABC is currently trading at $50. Using the quarterly EPS values shown below. Calculate the trailing P/E and
#forward P/E ratios

#   Past 12 months        Next 12 months 
#   -----------------   ----------------
#   |Quarter|EPS    |   |Quarter|EPS    |
#   -----------------   ----------------
#   |   Q1  |$0.75  |   |   Q1  |$0.82  |  
#   |   Q2  |$0.60  |   |   Q2  |$0.65  |
#   |   Q3  |$1.10  |   |   Q3  |$1.08  |
#   |   Q4  |$0.95  |   |   Q4  |$1.15  |
#   -----------------    ----------------

print(f"\nTrailing P/E ratio of ABC = {PEr(50,0.75+0.6+1.1+0.95)}")
print(f"\nForward P/E ratio of ABC = {PEr(50,0.82+0.65+1.08+1.15)}")
