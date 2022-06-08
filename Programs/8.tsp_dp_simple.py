n = 4

dist_matrix = [[0, 10, 15, 20], [10, 0, 35, 25],
			  [15, 35, 0, 30], [20, 25, 30, 0]]
	
start = 0

s = set(range(n)) - {start}
cost_table = [[9999 for _ in range(n)] for _ in range(n)]
def tsp(i, s):
	global dist_matrix
	if not s:
		return(dist_matrix[i][0])

	k_list = []
	minimum = 99999
	k_min = -1
	for k in s:
		k_list.append(k)
		temp = dist_matrix[i][k] + tsp(k, s - {k})
		if temp < minimum:
			minimum = temp
			k_min = k

	cost_table[k_min][i] = minimum
	return minimum

min_cost = tsp(start, s)
path = [0 for _ in range(n)]
print(f"Minimum Cost Of Traveling: {min_cost}")

# cost table
print(*cost_table,sep="\n")
# printing path
j = n - 1
while j > 0:
	for costs in cost_table:
		i = costs.index(min(costs))
		path[j] = i
		j -= 1

print(path)