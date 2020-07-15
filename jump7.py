for i in range(1,101):
	if i % 7 == 0:
		continue
	else:
		j = i
		while j != 0:
			if j %10 == 7:
				break
			j /= 10
		if j != 0:
			continue
	print(i)
