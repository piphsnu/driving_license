nat = input ('please input your nationality (Taiwan/USA):')
age = input ('please input your age:')
age = int (age)  # casting from string to integer
if nat == 'Taiwan': # setup Taiwan condition
	if age >= 18:
		print ('You can apply for driving license exam')
	else:
		print ('You cannot apply for driving license exam')
if nat == 'USA': # setup USA condition
	if age >= 16:
		print ('You can apply for driving license exam')
	else:
		print ('You cannot apply for driving license exam')
else: # other nationality
	print ('Your nationality must be input as either Taiwan or USA')
