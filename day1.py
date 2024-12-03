left_list = []
right_list = []
total_distance = 0

with open("input", "r") as f:
    line_list = []
    for line in f:
        line_list = line.split("   ")
        left_list.append(int(line_list[0]))
        right_list.append(int(line_list[1]))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
   total_distance += abs(left_list[i] - right_list[i])

print(total_distance)
