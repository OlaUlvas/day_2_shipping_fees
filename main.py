
"""

shipping fees

0 SEK < 300 < 250 SEK
250 SEK <= 275 < 500 SEK
500 SEK <= 225 < 750 SEK
750 SEK <= 125 < 1000 SEK
1000 SEK <= 0 SEK

> 250 SEK = 300 SEK
<= 250 SEK < 500 SEK = 275 SEK
<= 500 SEK < 750 SEK = 225 SEK
<= 750 SEK < 1000 SEK = 125 SEK
<= 1000 SEK = 0 SEk

"""


order = float(input("How much was the total price?: "))
fee = 0

if order < 250:
    fee = 300
elif order < 500:
    fee = 275
elif order < 750:
    fee = 225
elif order < 1000:
    fee = 125
else:
    fee = 0


price = round(order + fee, 2)

print(f"You have to pay {price} SEK.")