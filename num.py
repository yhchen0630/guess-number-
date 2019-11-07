import random
r = random.randint(1, 100)
number = 16
while True:
    num = input('猜數字：')
    num = int(num)
    if num == number:
        print('你猜對了')
        break
    elif num < 16 :
        print('你猜錯了，數字較大', input('繼續猜'))
    elif num > 16:
        print('你猜錯了，數字較小', input('繼續猜'))
    else:
        print('數字介於1~100之間', input('繼續猜'))