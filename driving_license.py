nat = input ('please input your nationality (Taiwan/USA):')
age = input ('please input your age:')
age = int (age)  # casting from string to integer
if nat == 'Taiwan':
	if age >= 18:
		print ('You can apply for driving license exam')
	else:
		print ('You cannot apply for driving license exam')
