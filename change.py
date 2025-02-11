## VG Task Change back 
## amount of bills and coins


a = float(input("enter price: ")) # float because the price can have decimal
b = int(input("enter payment: ")) # can use both float and int depands if its card or cash

change = round(b-a)  # math to get amount change

# We use here modulas and left overs of modulas 
# We use same process till we get our last 1 coin
# We used just round to not get and decimal otherwise round(d, amount od decimal)

thousand_bill = change//1000 
rest0= change%1000

five_hudred = rest0//500
rest1 = rest0 % 500

two_hundred = rest1 // 200
rest2 = rest1 % 200

hundred = rest2//100
rest3 = rest2%100

fiffty_bills= rest3//50
rest4 = rest3%50

twenty_bills =rest4//20
rest5= rest4%20

ten_coins =  rest5//10
rest6 = rest5%10

five_coins= rest6//5
rest7 = rest6%5

two_coins = rest7//2
rest8=rest7%2

one_coins = rest8//1
rest9 = rest8%1

# Printing our change + bill and coin system and amount of them.

print("change:", change) 
print("\n1000kr\t", thousand_bill, "\n500kr\t", five_hudred,"\n200kr\t", two_hundred, "\n100kr\t" ,hundred, "\n50kr\t", fiffty_bills, "\n20kr\t", twenty_bills, "\n10kr\t", ten_coins, "\n5kr\t", five_coins,"\n2k\t", two_coins, '\n1kr\t', round(one_coins))