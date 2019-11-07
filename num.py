import random
r = random.randint(1, 100)
count = 0
while True:
    count +=1 # count = count +1 
    num = input('猜數字：')
    num = int(num)
    if num == r:
        print('你猜對了')
        break
    elif num < r :
        print('你猜錯了，比答案較大')
    elif num > r :
        print('你猜錯了，數字較小')
    print('這是你第', count, '次')