# 동전의 종류 개수 n, 목표 금액 k 입력
n, k = map(int, input().split())

# 동전 단위를 저장할 리스트
coins = []

# 동전 단위 n개 입력 받기
for i in range(n):
    coins.append(int(input()))

# 사용할 동전 개수 누적 변수
ans = 0

# 가장 큰 동전부터 사용하기 위해 역순으로 반복
for i in range(n - 1, -1, -1):
    ans += k // coins[i]  # 해당 동전으로 몇 개 쓸 수 있는지 계산
    k %= coins[i]         # 해당 동전을 쓰고 남은 금액으로 갱신

# 최소 동전 개수 출력
print(ans)