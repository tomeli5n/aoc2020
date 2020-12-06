
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

print("Result: ",result)