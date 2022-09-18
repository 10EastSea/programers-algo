# 아이템 줍기
from collections import deque

MAP_SIZE = 51 * 2

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    # map 초기화
    map = [[1 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    for r in rectangle:
        start_x, start_y, end_x, end_y = r
        
        # map 2칸씩 띄어서 그리기
        for x in range(start_x, end_x):
            if map[x*2][start_y*2] != 2: map[x*2][start_y*2] = 0
            if map[x*2+1][start_y*2] != 2: map[x*2+1][start_y*2] = 0
            if map[x*2][end_y*2] != 2: map[x*2][end_y*2] = 0
            if map[x*2+1][end_y*2] != 2: map[x*2+1][end_y*2] = 0
        for y in range(start_y, end_y):
            if map[start_x*2][y*2] != 2: map[start_x*2][y*2] = 0
            if map[start_x*2][y*2+1] != 2: map[start_x*2][y*2+1] = 0
            if map[end_x*2][y*2] != 2: map[end_x*2][y*2] = 0
            if map[end_x*2][y*2+1] != 2: map[end_x*2][y*2+1] = 0
        map[end_x*2][end_y*2] = 0
        
        # 사각형 내부 색칠
        for x in range(start_x*2+1, end_x*2):
            for y in range(start_y*2+1, end_y*2): map[x][y] = 2
    # for line in map: print(line)
    
    visited = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    visited[characterX*2][characterY*2] = 1
    que = deque([(characterX*2, characterY*2, 0)]) # (x, y, 이동 거리)
    
    while que:
        x, y, move_cnt = que.popleft()
        
        if x == itemX*2 and y == itemY*2: # 도착했을 때
            answer = move_cnt; break
            
        for i in range(4):
            check_x, check_y, next_x, next_y = x+dx[i], y+dy[i], x+dx[i]*2, y+dy[i]*2
            if 0 <= next_x and next_x < MAP_SIZE and 0 <= next_y and next_y < MAP_SIZE:
                if map[check_x][check_y] == 0 and visited[next_x][next_y] == 0: # 이동할 수 있는 길이면서, 방문하지 않은 길
                    visited[next_x][next_y] = 1
                    que.append((next_x, next_y, move_cnt+1))
    
    return answer