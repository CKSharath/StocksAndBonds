# Price to Book (P/B) = MarketCap/BookValue

def ptob(MarketCap,BookValue):
    return MarketCap/BookValue
#1.A certain company has a MarketCap of $800M and a book value of $200M.It has 100M share_out 
#a) P/B=?
#b)book value per share=?
#c)price od stock=?
print(f"\na)P/B = {ptob(800,200)}")
print(f"\nb)B/S = {ptob(200,100)}$/share")
print(f"\nc)shares=MarketCap/share_out={800/100}")

#2.Company X has $4.5B in tangible assets and $2.1B in total liabilities. This company has $600M shares outstanding.
#Stack X is currently trading at $30
#a) BookValue=?
#b)B/S=?
#c)P/B=?

print(f"\na)BookValue = TangibleAssets-IntangibleAssets = 4.5 - 2.1 = ${4.5-2.1}B")
print(f"\nb)B/S={((4.5-2.1)*1000000000)/(600*1000000)}")
print(f"\nc)P/B={(600*1000000*30)/((4.5-2.1)*1000000000)}")

#Company ABC has a MarketCap of $8B and a P/B ratio of 4. It has 500M share_out.
#a)What is the book value for this company?
#b)Share price=?
#c)B/S=?
print(f"\na)BookValue ={(8*1000000000)/4}")
print(f"\nb)Share price = {8*1000000000/(500*1000000)}")
print(f"\nc)B/S={((8*1000000000)/4)/(500*1000000)}")

#undervalued 
#P/B<1 or P<B/S ot MC<BookValue

#overvalued
#P/B>1 or P>B/S ot MC>BookValue
