import random
r = random.randint(1, 100)
while True:
    num = input('猜數字：')
    num = int(num)
    if num == r:
        print('你猜對了')
        break
    elif num < r :
        print('你猜錯了，比答案較大')
    elif num > r:
        print('你猜錯了，數字較小')
    else:
        print('數字介於1~100之間')