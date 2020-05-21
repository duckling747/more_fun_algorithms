from sys import stdin
import heapq

previous = {}

def dijkstra(starting_vertex, adj_list, V) -> list:
    distances = [float('inf') for _ in range(V)]
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        print('processing vertex: ' + str(current_vertex))
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    return distances


V = int(input('vertex count: '))
E = int(input('edge count: '))
starting_vertex = int(input('starting vertex: '))
print()

adj_list = [[] for _ in range(V)]

for _ in range(E):
    a, b, dist = stdin.readline().rstrip().split(' ')
    adj_list[int(a)].append( (int(b), int(dist)) )
    adj_list[int(b)].append( (int(a), int(dist)) )

print('distances: ' + str(dijkstra(starting_vertex, adj_list, V)))
print('preceding nodes: ' + str(previous))
