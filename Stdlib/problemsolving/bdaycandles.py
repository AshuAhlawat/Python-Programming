def bdaycakecandles(arr):
    tallest_candle = max(arr)
    count = 0
    for i in arr:
        if i == tallest_candle:
            count += 1
        else:
            count += 0
    print(count)

bdaycakecandles([6,6,3,2,1,6])