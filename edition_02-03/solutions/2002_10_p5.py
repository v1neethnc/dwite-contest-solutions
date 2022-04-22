# October 2002, Problem 5: OFF TO THE OFFICE
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2002_10_problem5.txt") as file_data:
	data = file_data.read().split("\n")
	data = [int(i) for i in data]
	for k in data:
		for m in range(1, k):
			students = [i for i in range(1, k+1)]
			removed_order = []
			to_remove = 0
			removed_order.append(students[to_remove])
			students.remove(students[to_remove])
			while len(students) > 0:
				to_remove = to_remove + m -1
				if to_remove >= len(students):
					to_remove = to_remove % len(students)
				removed_order.append(students[to_remove])
				students.remove(students[to_remove])
			if removed_order[-1] == 13:
				print(m)
				break