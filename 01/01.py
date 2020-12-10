
with open("input.txt", "r") as f:
	lines = f.readlines()


for line in lines:
	_a = int(line)

	for i in range(len(lines)):
		_b = int(lines[i])
		sum = _a + _b
		if sum==2020:
			print("\t", _a, " + ", _b, " <---")
			result=_a*_b

print("Result part 1: ",result)

for line in lines:
	_a = int(line)

	for i in range(len(lines)):
		_b = int(lines[i])

		for j in range(len(lines)):
			_c = int(lines[j])
			sum = _a + _b + _c

			if sum==2020:
				print("\t", _a, " + ", _b, " + ", _c, " <---")
				result_b=_a*_b*_c

print("Result part 2: ",result_b)
