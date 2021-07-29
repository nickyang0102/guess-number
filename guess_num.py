# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random
a = input('請輸入最小範圍的數值')
b = input('請輸入最大範圍的數值')
a = int(a)
b = int(b)

r = random.randint(a, b)
count = 0
while True:
	count += 1
	num = input('請輸入範圍內的數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('比答案大唷')
	elif num < r:
		print('比答案小唷')
	print ('這是你猜的第', count, '次')


