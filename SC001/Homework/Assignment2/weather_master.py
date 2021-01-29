"""
File: weather_master.py
Name: Chia-Lin Ko
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	This program asks temperature from user to compute the
	highest temperature, lowest temperature, average temperature,
	and cold days (temperature < 16 deg. Celsius) among the inputs.
	Type the Exit value to leave the program.
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? ')) #  [degrees Celsius]
	if temperature == EXIT:
		print('No temperature were entered.')
	else:
		highest      = temperature
		lowest       = temperature
		sum          = temperature
		num          = 1
		num_cold_day = find_cold_day_num(0, temperature)
		while True:
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temperature == EXIT:
				break
			else:
				highest      = find_highest(temperature, highest)
				lowest       = find_lowest(temperature , lowest)
				sum         += temperature
				num         += 1
				num_cold_day = find_cold_day_num(num_cold_day, temperature)
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = '  + str(lowest))
		print('Average = '             + str(sum/num))
		print(str(num_cold_day)        + ' cold day(s)')

def find_highest(n1, n2):
	"""
	This function aims to find the highest value between n1 and n2

	:param n1: int, the number to be compared
	:param n2: int, the number to be compared
	:return: int, the highest one between n1 and n2
	"""
	if n1 > n2:
		return n1
	else:
		return n2

def find_lowest(n1, n2):
	"""
	This function aims to find the lowest value between n1 and n2

	:param n1: int, the number to be compared
	:param n2: int, the number to be compared
	:return: int, the lowest one between n1 and n2
	"""
	if n1 < n2:
		return n1
	else:
		return n2

def find_cold_day_num(num, temp):
	"""
	This function aims to find the number of cold day(s).
	The cold day mean the temperature lower than 16 degrees Celsius.

	:param num:  int, the number of cold day(s) before comparison
	:param temp: int, the temperature of the compared day
	:return:     int, the total number of cold day(s)
	"""
	if temp < 16:
		return num+1
	else:
		return num


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
