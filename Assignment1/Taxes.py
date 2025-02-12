## VG Task to implement a swedish simple tax system 

Enter=input("enter your salary:")
n=float(Enter)

T_amount1=38000            # tax amount 38000 
T_amount2=50000            # tax amount 50000

tax_30percent=(n*0.3)      # 30% tax percentage

af0=T_amount1*0.3    #Tax amount multiplied with percentage 
af1=(n-T_amount1)*0.35  #first amount 1 - rest of amount to get further 5% tax on it

af0=(T_amount1*0.3)
af4=af0+(T_amount2-T_amount1)*0.35
af5=(af4+(n-T_amount2)*0.4)      #first amount*30% + 5% + further 5% tax 

#useing if, elif and else to get right the right answer and for tax intervall
if n < tax_30percent:
    print("your tax amout is:", round(tax_30percent) )
elif tax_30percent < n and n < T_amount2:
    print("your tax amount is:", round(af0+af1))
else:
    print("your tax amountis:", round(af5))






    