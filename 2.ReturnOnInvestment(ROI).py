def roi(initial,final):
    return (final-initial)/initial*100

def annualROI(initial,final,years):
    return roi(initial,final)/years

# John purchases a home for $250,000 in 2019. 5 years later, he sells it for $325,000. 
# What is John's return on investment?
print("\nFor John : ")
print(f"ROI is {roi(250000,325000)} %")
print(f"Annual ROI is {annualROI(250000,325000,5)} % per year")

# Karen purchases 500 shares of stock at $20. The stock rises $27 in 3 months. What is Karen's ROI?
print("\nFor Karen : ")
print(f"ROI is {roi(500*20,500*27)}%")
print(f"Annual ROI is {annualROI(500*20,500*27,3/12)}%")

# Luke and James are looking to generate income from rental property. They both have
# $100,000 to invest with Luke buys a 2-bedroom condo for $100,000 and
# earns a net profit of $1000 per month by renting the condo. James somehow
# manages to buy four 2-bedroom condos for a total of $100,000 or $25,000 each
# He earns $1000 per month in net profit for each condo. What is the annual ROI for 
# Luke and James?

#The annual rental income formula is different 
def rentalAnnualROI(annualIncome,investment):
    return annualIncome/investment*100

print("\nFor Luke : ")
print(f"Annual rental ROI is {rentalAnnualROI(1000*12,100000)}%")

print("\nFor James : ")
print(f"Annual rental ROI is {rentalAnnualROI(4000*12,100000)}%")

#Susan buys a 2-bedroom condo for $80,000 in 2019. She rents it to a tenant and earns a net profit of $1000 per month.
#She sells the condo for $160,000 in 2029. During this 10 years period, she recieved $1000 per month for every month in 
#rental income 
#a)What is her total ROI generated from rental income only
#b)What is the total ROI generated from the sale of her property
#c)Calculate the total ROI and average annual ROI from both the sale of the property and her rental income
print("\nFor Susan : ")
print(f"\ntotal ROI generated from rental income only {10*rentalAnnualROI(12*1000,80000)}")
print(f"\nthe total ROI generated from the sale of her property {roi(80000,160000)}")
print(f"\nthe total ROI and average annual ROI from both the sale of the property and her rental income {rentalAnnualROI(12*1000,80000)+annualROI(80000,160000,2029-2019)}")
