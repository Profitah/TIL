import heapq

def dijkstra(start, graph):
    INF = float('inf')  # 무한대로 초기화
    dist = [INF] * len(graph)
    dist[start] = ____
    q = [(____, start)]

    while q:
        cost, now = ______(q)
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            if dist[nxt] > cost + w:
                dist[nxt] = ______
                ______(q, (dist[nxt], nxt))

    return dist
