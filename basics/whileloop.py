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

#

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_count=0
sum_count=0
len_num_list=len(num_list)
i=0
while (odd_count<5)&(i<len_num_list):
    if num_list[i] % 2!=0:
        sum_count+=num_list[i]
        odd_count+=1
    i+=1
print("The Summation of {} numbers added:{} ".format(odd_count,sum_count))
