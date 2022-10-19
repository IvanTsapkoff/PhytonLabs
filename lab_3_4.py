n = int(input('Введите число:'))
for i in range(1, n+1):
	for p in range(1, n-i+1):
		print(' ', end = '')
	for c1 in range(1, i+1):
		print(c1, end = '')
	for c2 in range(i-1, 0, -1):
		print(c2, end = '')
	print()
