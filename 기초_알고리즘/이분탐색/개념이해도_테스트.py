import sys
read_input = sys.stdin.readline

def binary(arr, target):
    pl, pr = 0, len(arr) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        if arr[pc] == target:
            return True
        elif arr[pc] < target:
            pl = pc + 1
        else:
            pr = pc - 1
    return False

# 입력
n_a, n_b = map(int, read_input().split())
arr_A = list(map(int, read_input().split()))
arr_B = list(map(int, read_input().split()))

# B 정렬
arr_B.sort()

# A의 원소 중 B에 없는 것만 추려냄
result = []
for a in arr_A:
    if not binary(arr_B, a):
        result.append(a)

# 정렬해서 출력
result.sort()
print(len(result))
if result:
    print(' '.join(map(str, result)))