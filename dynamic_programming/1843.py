# 사칙연산
INF = 101 * 1000

def solution(arr):
    answer = -1
    
    num_cnt = (len(arr) // 2) + 1 # 전체 숫자 개수
    
    max_dp = [[-INF for _ in range(num_cnt)] for _ in range(num_cnt)] # max_dp[i][j] = i번째 숫자부터 j번째 숫자까지 연산했을 때 최대값
    min_dp = [[INF for _ in range(num_cnt)] for _ in range(num_cnt)] # min_dp[i][j] = i번째 숫자부터 j번째 숫자까지 연산했을 때 최소값
    for i in range(num_cnt):
        max_dp[i][i] = int(arr[i*2])
        min_dp[i][i] = int(arr[i*2])
    
    for cnt in range(num_cnt):
        for i in range(num_cnt - cnt):
            j = i + cnt
            for k in range(i, j):
                if arr[k*2+1] == "+": # + 연산자일 때
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else: # - 연산자일 때
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
    
    # for line in max_dp:
    #     print(line)
    # print(max_dp[0][num_cnt-1])
    answer = max_dp[0][num_cnt-1]
    
    return answer