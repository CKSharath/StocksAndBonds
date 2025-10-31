def roi(initial,final):
    return (final-initial)/initial*100

def annualROI(initial,final,years):
    return roi(initial,final)/5

# John purchases a home for $250,000 in 2019. 5 years later, he sells it for $325,000. 
# What is John's return on investment?
print("\nFor John : ")
print(f"ROI is {roi(250000,325000)} %")
print(f"Annual ROI is {annualROI(250000,325000,5)} % per year")

# Karen purchases 500 shares of stock at $20. The stock rises $27 in 3 months. What is Karen's ROI?
print("\nFor Karen : ")
print(f"ROI is {roi(500*20,500*27)}%")
print(f"Annual ROI is {4*roi(500*20,500*27)}%")

# Luke and James are looking to generate income from rental property. They both have
# $100,000 to invest with Luke buys a 2-bedroom condo for $100,000 and
# earns a net profit of $1000 per month by renting the condo. James somehow
# manages to buy four 2-bedroom condos for a total of $100,000 or $25,000 each
# He earns $1000 per month in net profit for each condo. What is the annual ROI for 
# Luke and James?

print("\nFor Luke : ")
print(f"ROI is {roi(100000,1000)}%")
print(f"Annual ROI is {12*roi(100000,1000)}%")

print("\nFor James : ")
print(f"ROI is {roi(25000,1000)}%")
print(f"Annual ROI is {12*roi(25000,1000)}%")
