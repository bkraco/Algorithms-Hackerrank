import sys
from heapq import *


def read(fn):
    return tuple(fn(i) for i in sys.stdin.readline().split(' '))


def load_graph(A, B):
    
    #Builds an adjacency list representation of a graph with A vertices.
   
    graph = [dict() for i in range(0, A)]

    for i in range(0, B):
        (x, y, r) = read(int)
        x -= 1
        y -= 1

        # Ignore all edges except minimum length.
        r = r if y not in graph[x] else min(r, graph[x][y])
        graph[x][y] = r
        graph[y][x] = r

    return graph


def dijkstras(graph, source):
    """
    Dijkstras alg on the graph starting at the source vertex. Returns a list
    of distances from the source to all other nodes. -1: No path exists.
    """
    q = []
    heappush(q, (0, source))

    distances = [-1] * len(graph)
    distances[source] = 0

    while len(q) > 0:
        (distance, vertice) = heappop(q)

        # Ignore this distance if a shorter path has been found for this node.
        if distances[vertice] > 0:
            continue
        distances[vertice] = distance

        # Queue up all unvisited neighbors.
        for n in graph[vertice]:
            if distances[n] > -1:
                continue
            cost = distance + graph[vertice][n]
            heappush(q, (cost, n))

    return distances


def test():
    (A, B) = read(int)
    graph = load_graph(A, B)

    S = read(int)[0] - 1
    distances = dijkstras(graph, S)

    for i in range(0, A):
        if i != S:
            end = ' ' if i < n - 1 else '\n'
            print(distances[i], end=end)


def main():
    T = read(int)[0]
    for i in range(0, T):
        test()

if __name__ == '__main__':
    main()

t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    for a1 in range(m):
        x,y,r = input().strip().split(' ')
        x,y,r = [int(x),int(y),int(r)]
    s = int(input().strip())
