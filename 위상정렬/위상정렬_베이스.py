import sys
import heapq

input = sys.stdin.readline

# 입력 받기: 학생 수 n, 관계 수 m
n, m = map(int, input().split())

# 그래프 초기화
graph = []
for i in range(n + 1):
    graph.append([])

# 진입차수 배열 초기화
indegree = []
for i in range(n + 1):
    indegree.append(0)

# 간선 정보 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)      # a → b
    indegree[b] += 1        # b는 a 앞에 서야 하므로 진입차수 +1

# 우선순위 큐 사용 (번호가 작은 노드부터 꺼내기 위함)
heap = []
for i in range(1, n + 1):
    if indegree[i] == 0:          # 진입차수가 0인 노드
        heapq.heappush(heap, i)   # 큐에 추가

# 위상 정렬 결과 저장용 리스트
result = []

# 큐가 빌 때까지 반복
while heap:
    current = heapq.heappop(heap)  # 가장 앞에 설 수 있는 노드 꺼냄
    result.append(current)         # 결과에 추가

    # 현재 노드가 가리키는 노드들 순회
    for next in graph[current]:
        indegree[next] -= 1        # 진입차수 감소
        if indegree[next] == 0:
            heapq.heappush(heap, next)  # 이제 앞에 설 수 있으므로 큐에 추가

# 결과 출력
for i in result:
    print(i, end=' ')
