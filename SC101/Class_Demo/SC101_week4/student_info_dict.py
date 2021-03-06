"""
File: student_info_dict.py
Name: Chia-Lin Ko
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info.
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################
	with open(FILE, 'r') as f:
		for line in f:
			info_list = line.split()
			name  = info_list[0]
			age   = info_list[1]
			email = info_list[2]
			food  = info_list[3:]

			student_d = {}
			#print(hex(id(student_d)))
			student_d['AGE']   = age
			student_d['EMAIL'] = email
			student_d['FOOD']  = food

			all_d[name] = student_d

	######################
	#print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This method prints out a nested data structure on console
	"""
	for name, name_d in d.items():
		print(name)
		print(name_d)
		print('---------------------------------')


if __name__ == '__main__':
	main()
