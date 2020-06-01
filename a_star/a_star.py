import heapq
from random import uniform
from sys import stdin


# heuristic for distance (just random for now)
def h(vertex):
    return uniform(0, 1)


def reconstructpath(prev, current, a, b):
    path = [current]
    while current in prev.keys():
        current = prev[current]
        path.append(current)

    return path[::-1], a, b


def astar(start, target, adj_list, V):
    openset = []
    heapq.heappush(openset, (float('inf'), start))
    prev = {}
    gscore = [float('inf') for _ in range(V)]
    gscore[start] = 0
    fscore = [float('inf') for _ in range(V)]
    fscore[start] = h(start)
    while openset:
        distance, current = heapq.heappop(openset)
        if current == target:
            return reconstructpath(prev, current, distance - 1, distance)

        for neighbor, d in adj_list[current]:
            tentativegscore = gscore[current] + d
            if tentativegscore < gscore[neighbor]:
                prev[neighbor] = current
                gscore[neighbor] = tentativegscore
                fscore[neighbor] = gscore[neighbor] + h(neighbor)
                if neighbor not in openset:
                    heapq.heappush(openset, (fscore[neighbor], neighbor))
    return False


V = int(input('vertex count: '))
E = int(input('edge count: '))
starting_vertex = int(input('starting vertex: '))
target = int(input('target vertex: '))
print()

adj_list = [[] for _ in range(V)]

for _ in range(E):
    a, b, dist = stdin.readline().rstrip().split(' ')
    adj_list[int(a)].append((int(b), int(dist)))
    adj_list[int(b)].append((int(a), int(dist)))

print(('path', 'lower_bound', 'upper_bound'))
print(str(astar(starting_vertex, target, adj_list, V)))
