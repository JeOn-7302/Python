from collections import deque

def solution(players, m, k):
    active_servers = deque()
    total_additions = 0

    for t in range(24):
        # 1. 만료된 서버 제거
        while active_servers and active_servers[0] <= t:
            active_servers.popleft()

        # 2. 필요한 서버 수 계산
        need = players[t] // m
        current = len(active_servers)

        # 3. 부족한 서버 수만큼 증설 (1대당 1회로 계산됨)
        for _ in range(need - current):
            active_servers.append(t + k)
            total_additions += 1

    return total_additions
