import pickle

with open('data.pickle', 'rb') as file:
	output = pickle.load(file)

outputChar = ''

for array in output:
	for tupl in array:
		if tupl[0] == ' ':
			outputChar = ' '
		else:
			outputChar = '#'
		for i in range(int(tupl[1])):
			print(outputChar, sep=' ', end='', flush=True)
	print("\n")
