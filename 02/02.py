import re

with open("input.txt", "r") as f:
	lines = f.readlines()

# example = "1-5 z: mhkzwdxklf"

def analize(string):
	""" desarma el input en un obj """

	policy = {}
	#regex to translate
	_regex =  re.search('(^\d+)-(\d+)\s(\w(?=:)):\s(\w.*)', string)

	#print(re.group(0))
	_min = _regex.group(1)
	_max = _regex.group(2)
	letter = _regex.group(3)
	password = _regex.group(4)

	policy = {
		"min" : _min,
		"max" : _max,
		"letter" : letter,
		"password" : password
	}
	return policy

# test = analize(example)
# print(test)
count_result=0

for line in lines:

	crit = analize(line)

	# print(crit['password'])
	if(int(crit['min']) <= str(crit['password']).count(crit['letter']) <= int(crit['max']) ):
		# print(crit['password'], " cumple el criterio de al menos ", crit['min'], " ",crit['letter'])
		count_result +=1

print("Analized passwords: ", len(lines))
print("Part 1 Result: ",count_result)

""" part 2 : password position"""

count_result2 = 0

for line in lines:
	posi = analize(line)

	_posA = int(posi['min'])
	_posB = int(posi['max'])
	_letter = posi['letter']
	_pass = posi['password']

	# print(_pass,"-",_letter,"-",_posA,_posB)

	if(bool(_pass[_posA-1] == _letter) ^ bool(_pass[_posB-1] == _letter)):
		""" ^ es el operador XOR. bool() devuelve true or false """
		print(_pass, _letter, "Found!", _posA, "-",_posB)
		count_result2+=1

print("Part 2 Result: ",count_result2)
