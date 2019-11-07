import random
start = input('請輸入最小範圍值')
end = input('請輸入最大範圍值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count +=1 # count = count +1 
    num = input('猜數字：')
    num = int(num)
    if num == r:
        print('你猜對了', '這是你猜的第', count, '次')
        break
    elif num < r :
        print('你猜錯了，比答案較大', '這是你猜的第', count, '次')
    elif num > r :
        print('你猜錯了，數字較小', '這是你猜的第', count, '次')
