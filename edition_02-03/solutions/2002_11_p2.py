# November 2002, Problem 2: THE FIVE M's OF STATS
# https://github.com/v1neethnc/dwite-contest-solutions

with open("../inputs/2002_11_problem2.txt") as file_data:
	data = file_data.read().split("\n")
	ind = 0
	while ind < len(data)-1:
		ln = int(data[ind])
		vals = [float(i) for i in data[ind+1:ind+ln+1]]
		ind = ind + ln
		vals.sort()
		mean = sum(vals)/len(vals)
		if len(vals) % 2 == 1:
			median = vals[len(vals)//2]
		else:
			median = (vals[len(vals)//2 - 1] + vals[len(vals)//2]) / 2
		mode = max(set(vals), key=vals.count)
		mx, mn = max(vals), min(vals)
		for i in [mean, median, mode, mx, mn]:
			print(f"{i:.2f}")