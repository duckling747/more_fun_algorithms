from sys import stdin

class Edge:
    def __init__(self, fro, to, capacity, cost):
        self.fro = fro
        self.to = to
        self.capacity = capacity
        self.cost = cost
    def __repr__(self):
        return 'from: {} to: {} capacity: {} cost: {}'.format(self.fro, self.to, self.capacity, self.cost)

INF = float('inf')
edges = []
adj = []
cost = []
capacity = []


def shortest_paths(n, s, d, p):
    global adj, cost, capacity
    d[s] = 0
    inq = [False for _ in range(n)]
    q = []
    q.append(s)
    while len(q):
        u = q.pop(0)
        inq[u] = False
        if u > len(adj)-1:
            continue
        for v in adj[u]:
            if capacity[u][v] > 0 and d[v] > d[u] + cost[u][v]:
                d[v] = d[u] + cost[u][v]
                p[v] = u
                if not inq[v]:
                    inq[v] = True
                    q.append(v)

def min_cost_flow(N, K, s, t):
    global adj, cost, capacity
    adj = [[] for _ in range(N)]
    cost = [[0 for _ in range(N)] for _ in range(N)]
    capacity = [[0 for _ in range(N)] for _ in range(N)]
    for e in edges:
        adj[e.fro].append(e.to)
        adj[e.to].append(e.fro)
        cost[e.fro][e.to] = e.cost
        cost[e.to][e.fro] = -e.cost
        capacity[e.fro][e.to] = e.capacity
        capacity[e.to][e.fro] = 0

    flow = 0
    costv = 0
    while flow < K:
        d = [INF for _ in range(N)]
        p = [-1 for _ in range(N)]
        shortest_paths(N, s, d, p)
        if d[t] == INF:
            break
        f = K - flow
        cur = t
        while cur != s:
            f = min(f, capacity[p[cur]][cur])
            cur = p[cur]
        flow += f
        costv += f * d[t]
        cur = t
        while cur != s:
            capacity[p[cur]][cur] -= f
            capacity[cur][p[cur]] += f
            cur = p[cur]
    if flow <= K:
        return costv
    else:
        return -1

V = int(input('vertex count: '))
E = int(input('edge count: '))
s = int(input('starting vertex: '))
t = int(input('target vertex: '))
print()
for _ in range(E):
    a, b, cap, cost = stdin.readline().rstrip().split(' ')
    edges.append(Edge(fro=int(a), to=int(b), capacity=int(cap), cost=int(cost)))

print('edges:')
print(*edges, sep='\n')
print('starting from: {}, target is: {}'.format(s, t))
print('min cost is: ' + str(min_cost_flow(V+1, INF, s, t)))
