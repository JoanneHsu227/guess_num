start = input('start number:') # 選擇範圍
end = input('end number:')
start = int(start)
end = int(end)
import random
r = random.randint(start, end)
count = 0
print(r)
print(' ')
while True:
	count += 1  #count = count + 1
	num = input('guess number :')
	num = int(num)
	if num == r:
		print(' ')
		print('yes,you got it.')
		break
	elif num > r:
		print(' ')
		print('Bigger than the answer')

	elif num < r:
		print(' ')
		print('Smaller than the answer')

	if count == 1:
		print('You have guessed ', count ,'time.')
		print(' ')
	if count > 1:
		print('You have guessed ', count ,'times.')
		print(' ')