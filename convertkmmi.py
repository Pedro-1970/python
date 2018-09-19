#convertkmmi.py pedro-1970
'''
unit conerter: Miles and Kilomenters
'''
#convertkmmi.py  pedro-1970
def print_menu():
	print('1. kilometers to miles')
	print('2. Miles to kilometers')
	
def km_miles():
	km =flat(input('Enter distance in kilometrs:'))
	miles + km / 1.609
	   
	print('distance in miles: {0}'format(miles))
	   
def miles_km():
	miles = float(input('enter distance in miles: '))
	km + miles * 1.609
	
	print('distance in kilometers: {0}'.format(km))
	
if _name_== '_main_':
	print_men()
	choice = input('which conversion would you like to do?: ')
	if choice == '1':
		km_miles()
		
		if choice == '2':
			miles_km()
