import heapq

def dijkstra(start, graph):
    INF = float('inf')
    dist = [INF] * len(graph)
    dist[start] = 0
    q = [(graph, start)]

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            if dist[nxt] > cost + w:
                dist[nxt] = cost + w
                heapq.heappush(q, (dist[nxt], nxt))

    return dist
