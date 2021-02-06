"""
File: file_reading.py
Name: Chia-Lin Ko
---------------------------
This file shows how we can open and
print text files through Python code
"""


def main():
	filename_list = ['text/JerrySecret1.txt',
					 'text/JerrySecret2.txt',
					 'text/JerrySecret3.txt',
					 'text/JerrySecret4.txt']

	for filename in filename_list:
		print('\nFilename: ', filename)
		with open(filename, 'r') as f:
			for line in f:
				print(line, end='')



if __name__ == '__main__':
	main()
