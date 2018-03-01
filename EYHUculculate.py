print("Ноль в качестве знака операции завершит работу программы")
while True:
	s = input("Знак (and,or,xor,not): ")
	if s == '0': break
	if s in ('and','or','xor','not'):
		x = int(input("x="))
		y = int(input("y="))
		if s == 'and':
			print("%.2f" % (x&y))
		elif s == 'or':
			print("%.2f" % (x|y))
		elif s == 'xor':
			print("%.2f" % (x^y))
		elif s == 'not':
			if y != 0:
				print("%.2f" % (~x))
			else:
				print("Деление на ноль!")
	else:
		print(+"Неверный знак операции!")