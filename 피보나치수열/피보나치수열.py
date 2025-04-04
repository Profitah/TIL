# 피보나치 수열을 탑다운 형식과 바텀업 형식으로 출력하는 프로그램
memo = {} # 딕셔너리형식으로 memo 선언 # 메모이제이션을 위한 딕셔너리
def top_down(n): # n을 매개변수로 받는 함수 top_down
    if n <= 1: # n이 1보다 작거나 같으면 
        return n # n을 반환. # 여기서 n은 피보나치 수열을 n번째 항
    if n in memo: # n이 memo에 있으면
        return memo[n] # memo [n]을 반환
    
    memo[n] = top_down(n - 1) + top_down(n - 2) # memo[n]에 top_down(n - 1) + top_down(n - 2)를 저장
    return memo[n] # memo[n]을 반환 # memo[n]은 피보나치 수열을 n번째 항


def bottom_up(n): # n을 매개변수로 받는 함수 bottom_up
    if n == 0: # n이 0이면
        return 0 # 0을 반환
    dp = [0] * (n + 1) # dp를 0으로 초기화 # dp는 피보나치 수열을 저장하는 리스트
    dp[1] = 1 # dp[1]을 1로 초기화 # dp[1]은 피보나치 수열의 첫 번째 항
    for i in range(2, n + 1): # i를 2부터 n까지 반복
       dp[i] = dp[i -1] + dp[ i - 2] # dp[i]에 dp[i - 1] + dp[i - 2]를 저장 # dp[i]는 피보나치 수열의 i번째 항
    return dp [n] # dp[n]을 반환 # dp[n]은 피보나치 수열의 n번째 항