# 방의 개수
from collections import defaultdict

# 해답 참고함..
def solution(arrows):
    answer = 0
    
    x, y = 0, 0
    dx, dy = [0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1]
    visited = defaultdict(list)
    
    for arrow in arrows:
        for _ in range(2): # 대각선으로 겹쳐서 생기는 방 detect -> 두번씩 이동하는걸로 해결
            nx, ny = x+dx[arrow], y+dy[arrow] # 다음 이동할 경로 찾기
            
            if (nx,ny) in visited and (x,y) not in visited[(nx, ny)]: # 방문한 경우 + 중복된 경로가 아닌 경우
                answer += 1
                visited[(nx, ny)].append((x, y))
                visited[(x, y)].append((nx, ny))
            elif (nx, ny) not in visited: # 방문하지 않은 경우
                visited[(nx, ny)].append((x, y))
                visited[(x, y)].append((nx, ny))
            # 중복된 경로인 경우는 따로 처리 해주지 않아도 됨
            
            x, y = nx, ny # 다음 이동할 경로로 이동
    
    return answer