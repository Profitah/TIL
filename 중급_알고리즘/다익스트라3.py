import heapq

def dijkstra(start, graph):
<<<<<<< HEAD
    INF = float('inf')
    dist = [INF] * len(graph)
    dist[start] = 0
    q = [(graph, start)]

    while q:
        cost, now = heapq.heappop(q)
=======
    INF = float('inf')  # 무한대로 초기화
    dist = [INF] * len(graph)
    dist[start] = ____
    q = [(____, start)]

    while q:
        cost, now = ______(q)
>>>>>>> 591e993e081af535a421035aa95dd1cfb3050971
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            if dist[nxt] > cost + w:
<<<<<<< HEAD
                dist[nxt] = cost = w
                heapq.heappush(q, (dist[nxt], nxt))

    return dist
=======
                dist[nxt] = ______
                ______(q, (dist[nxt], nxt))

    return dist
>>>>>>> 591e993e081af535a421035aa95dd1cfb3050971
