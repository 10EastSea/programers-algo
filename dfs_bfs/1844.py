# 게임 맵 최단거리
from collections import deque 

def solution(maps):
    answer = 0
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    
    que = deque([(0, 0, 1)]) # (x, y, 이동 횟수)
    visited = [[0 for _ in range(m)] for _ in range(n)]; visited[0][0] = 1 # 방문 기록
    
    while que:
        x, y, move_cnt = que.popleft()
        
        if x == n-1 and y == m-1: # 도착했을 때
            answer = move_cnt; break
        
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if(0 <= next_x and next_x < n and 0 <= next_y and next_y < m):
                if(maps[next_x][next_y] == 1 and visited[next_x][next_y] == 0): # 이동할 수 있는 길이면서, 방문하지 않은 길
                    visited[next_x][next_y] = 1; que.append((next_x, next_y, move_cnt+1))
        
        if not que: # 도착하지 못했을 때
            answer = -1; break
    
    return answer