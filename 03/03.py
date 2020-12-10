""" Day 3: Toboggan Trajectory """
from math import ceil

with open("input.txt", "r") as f:
	lines = f.readlines()

x_pos=0
y_pos=0
iter =0
x_offset=3
y_offset=1
pines_result = 0

# prepare terrain
width = x_offset*len(lines)
print("Width = ", width)
print("largo = ", len(lines[0]))
duplicacion_necesaria = ceil(width / len(lines[0]))
print("duplicacion necesaria", duplicacion_necesaria)

""" estirar terreno. Pasé de 3 loops a uno sólo copiando el listado """
map = []
for j in range(len(lines)):
	map.append( lines[j].rstrip() * duplicacion_necesaria)


# print("\n###\n")

# for line in lines:
# 	print(line.rstrip())

# print("\n###\n")

for line in map:

	x_pos=x_offset*iter
	y_pos=y_offset*iter

	row = list(line.rstrip())
	if row[x_pos] == ".":
		layer = "O"
	else:
		layer = "x"
		pines_result += 1

	row[x_pos] = layer
	print("".join(row), iter)

	iter+=1

print()
print("Part 1 Result:", pines_result, "pinos chocados")

""" part 2 : password position"""

# print("Part 2 Result: ",count_result2)
