import heapq

def dijkstra(start, graph):
    INF = float('inf')  # 무한대로 초기화
    dist = [INF] * len(graph)  # 거리 배열
    dist[start] = 0  # 시작 노드는 0으로
    q = [(0, start)]  # 우선순위 큐 (거리, 노드)

    while q:
        cost, now = heapq.heappop(q)  # 가장 가까운 노드 꺼내기
        if dist[now] < cost:  # 이미 처리된 노드면 건너뜀
            continue
        for nxt, w in graph[now]:  # 인접 노드 탐색
            if dist[nxt] > cost + w:  # 더 짧은 거리 발견 시
                dist[nxt] = cost + w  # 거리 갱신
                heapq.heappush(q, (dist[nxt], nxt))  # 큐에 추가

    return dist  # 최종 거리 배열 반환