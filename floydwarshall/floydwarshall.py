from sys import stdin

def setup(V):
    return [ [float('inf') for i in range(V)] for j in range(V) ]

def floydwarshall(V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]


V = int(stdin.readline())

distances = setup(V)

for _ in range(V):
    line_arr = stdin.readline().rstrip().split(' ')
    distances[int(line_arr[0])][int(line_arr[1])] = int(line_arr[2])

floydwarshall(V)
print(distances)
