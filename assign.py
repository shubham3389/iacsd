#!/usr/bin/python3

def draw_line():
	print('-' *40)

def main():
	dict = {'DAC':240, 'DBDA':120, 'DITISS':60}
	print(dict)

	draw_line()
	print(sorted(dict))
	draw_line()
	
	dict1 = sorted([(value, key) for (key, value) in dict.items()])
	print("Sorted list by Value :")
	print(dict1)

# standard boiler plate syntax that calls the main() function

if __name__=='__main__':
        main()
