# Write a program birthday_candles
# that computes how many boxes of candles a person needs to buy each year
# for her\his birthday cake. 
# You can assume that the person reaches an age of 100, 
# the number of candles used each year is the same as the age, 
# that you save non-used candles from one year to another, 
# and that each box contains 24 candles.
# Also, at the end, we want you to print the total number of boxes one has to buy, and how many candles that are available after having celebrated the 100th birthday.


def calculate_candles_and_packets():
    total_candles_needed = sum(range(1, 101))  # Sum of numbers from 1 to 100
    candles_per_packet = 24
    total_packets = total_candles_needed // candles_per_packet
    leftover_candles = total_candles_needed % candles_per_packet

    # If there are leftover candles, we need one more packet
    if leftover_candles > 0:
        total_packets += 1
        leftover_candles = candles_per_packet - leftover_candles

    return total_packets, leftover_candles

total_packets, leftover_candles = calculate_candles_and_packets()

for year in range(1, 101):
    total_candles_needed = sum(range(1, year + 1))
    candles_per_packet = 24
    total_packets = total_candles_needed // candles_per_packet
    leftover_candles = total_candles_needed % candles_per_packet

    # If there are leftover candles, we need one more packet
    if leftover_candles > 0:
        total_packets += 1
        leftover_candles = candles_per_packet - leftover_candles

    print(f"Year {year}: Total packets needed: {total_packets}, Leftover candles: {leftover_candles}")