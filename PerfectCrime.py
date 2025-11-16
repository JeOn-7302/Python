from collections import defaultdict

def solution(info, n, m):
    # key: B의 흔적 누적합, value: A의 누적 흔적 최소값
    dp = {0 : 0}
    INF = float('inf')
    for a_trace, b_trace in info:
        next_dp = defaultdict(lambda : INF)     # 다음 상태 저장
        
        for b_sum, a_sum in dp.items():
            
            # A가 훔치면
            new_a = a_sum + a_trace
            new_b = b_sum
            if new_a < n and new_b < m:
                next_dp[new_b] = min(next_dp[new_b], new_a)
                
            # B가 훔치면
            new_a = a_sum
            new_b = b_sum + b_trace
            if new_a < n and new_b < m:
                next_dp[new_b] = min(next_dp[new_b], new_a)
                
        # 상태 갱신
        dp = next_dp
        
    # 가능한 모든 경우 중 A의 최소 흔적 반환
    if not dp:
        return -1
    
    else:
        return min(dp.values())