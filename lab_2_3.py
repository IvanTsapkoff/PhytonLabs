a = input('Введите первое число:\n')
b = input('Введите второе число:\n')
c = input('Введите третье число:\n')

if (a > b) and (a > c):
	print('Наибольшее:\n',a)
elif (b > a) and (b > c):
	print('Наибольшее:\n',b)
else:
	print('Наибольшее:\n',c)

