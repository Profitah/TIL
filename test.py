# https://www.youtube.com/watch?v=wwqS53DPMw0 보고 배움

import sys

n = int(input())  
A = list(map(int, input().split()))   
A.sort()   # 이진 탐색을 수행하려면 반드시 정렬해야 함

m =int(sys.stdin.readline().strip())  # 찾아야 할 숫자의 개수
B = list(map(int, sys.stdin.readline().split()))  # 찾고자 하는 숫자 리스트 (B)

# 이진 탐색 함수 (Binary Search)
def binary_search(target_from_b	, list_a):  
    """
    - target: 찾고자 하는 값 (B 리스트에서 가져옴)
    - arr: 탐색 대상 리스트 (A 리스트, 반드시 정렬된 상태여야 함)
    - 반환값: target이 arr 안에 있으면 True, 없으면 False
    """

    current_min = 0  # 탐색 범위의 시작점 (왼쪽 포인터, pl)
    current_max = n - 1  # 탐색 범위의 끝점 (오른쪽 포인터, pr)
    cursor = (current_min + current_max) // 2  # 현재 탐색할 중앙값 (pc)

    # 탐색 범위가 유효한 동안 반복
    while current_min <= current_max:  
        if list_a[cursor] == target_from_b	:  # 현재 중앙값이 찾는 값과 일치하면
            return True  # 탐색 성공 (True(1) 반환)
        
        elif list_a[cursor] < target_from_b	:  # 현재 중앙값이 찾는 값보다 작다면
            """
            - target은 중앙값보다 더 오른쪽에 있음
            - 왼쪽 부분은 탐색할 필요 없음 → current_min을 cursor + 1로 이동
            """
            current_min = cursor + 1  

        else:  # 현재 중앙값이 찾는 값보다 크다면
            """
            - target은 중앙값보다 더 왼쪽에 있음
            - 오른쪽 부분은 탐색할 필요 없음 → current_max를 cursor - 1로 이동
            """
            current_max = cursor - 1  

        # 새로운 탐색 범위를 반영하여 중앙값(cursor) 업데이트
        cursor = (current_max + current_min) // 2  

    return False  # 찾는 값이 없으면 False(0) 반환

# B 리스트의 각 숫자에 대해 A 리스트에서 존재 여부 확인
for i in range(m):  
    print(binary_search(B[i], A))  # 존재하면 True(1), 없으면 False(0) 출력