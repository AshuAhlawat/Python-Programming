#to explain while loop we will use an example to use while loop
card_deck=[4,11,8,5,13,2,8,10]
hand=[]

while sum(hand) <= 17 :
    hand.append(card_deck.pop())
print(hand)

#factorial with while loops
number=6
product=1
current=1
while current<=number:
    product*=current
    current +=1
print(product)