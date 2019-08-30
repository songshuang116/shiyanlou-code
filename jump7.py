for num in range(1,101):
	if num % 7 ==0:
		continue
	elif num>=70 and num<=79:
		continue
	elif (num-7) %10 ==0:
		continue
	else:
		print(num)

