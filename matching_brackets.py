# matching brackets - a VERY provisional approach
def validate(title):
	# go through a string, return false if brackets are:
	## unmatched - if not all the opening brackets are paired - invalid
	## in wrong order - if one of closing brackets appears first - invalid
	## in wrong order by type - if other bracket closes than opens
	## empty
	
	o_brackets = ['(','[','{']
	c_brackets = [')',']','}']
	stack = []
	last_br = 0
	
	for c in title:
		
		if len(stack) > 0:
			pass
		
		if c in o_brackets:
			stack.append(c)
			# last_br = title.index(c)
			last_br = len(stack)-1
			print(stack)
		
		if c in c_brackets and len(stack) == 0: 
			print('INV - closing bracket appeared before opening bracket')
			return False
		
		if c in c_brackets and ( o_brackets.index(stack[last_br]) != c_brackets.index(c) ):
			print('INV - closing bracket of different type appeared first')
			return False
			
		if c in c_brackets and ( title.index(c) - last_br < 2 ):
			print('INV - met empty brackets')
			return False
			
		if c in c_brackets and ( o_brackets.index(stack[last_br]) == c_brackets.index(c) ):
			stack.pop()
			last_br -= 1
			print('br match')
			
	
	if len(stack) > 0:
		print('INV - unmatched bracket left')
		return False
			
	print('VAL')
	return True	

			
validate('j(a)n[]s{}z')

# print('janusz'.index('s'))