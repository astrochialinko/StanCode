EXIT = '-1'


def main():
	
	stack = []
	while True:
		line = input('Your input (-1 to quit): ')

		if line == EXIT:
			break

		stack.append(line)

	# Reverse print
	while len(stack) != 0:
		print(stack.pop())


if __name__ == '__main__':
	main()