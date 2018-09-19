#find-factores.py pedro-1970
def factors(b):
	
	for i in range(1, b+1):
		if b % i == 0:
			print(i)
			
		if__name__ =='__main__':
				
			b = input('Your Number please: ')
			b = float(b)
				
			if b > 0 and b.is_intger():
				factors(int(b))
			else:
				print('Please enter a positve inter')
