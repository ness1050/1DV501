
## VG task to find the colour of a specific ChessBoard id

chess_square = input("type your chess identifier in this order (ex. e5): ")

chess = int(chess_square[1]) #we are inserting a value for the integer 

ch_letter= ord(chess_square[0]) #every alphbet/character has its own value 

# we know the a strings starts with index 0 
# so python should be able to read what index value a to g has
# so python should be able to know what value our digits hase from 1-8



# We use if elif and else to make python print what our chess square color is
# which we use if and elif for understing what value our intgar has and our pharses
# else we used for if and elif function is forfilled or not 
# result
if chess%2==0 and ch_letter %2!= 0:
    print(chess_square, "chess square is white" )
elif chess%2!=0 and ch_letter %2 ==0 :
    print(chess_square, "chess square is white ")
else:
    print("chess square is black")