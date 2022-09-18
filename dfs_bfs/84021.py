# 퍼즐 조각 채우기
from collections import deque

PUZZLE_SIZE = 6

def rotate_90(puzzle):
    new_puzzle = [[0 for _ in range(PUZZLE_SIZE)] for _ in range(PUZZLE_SIZE)]
    
    # 90도 회전
    for j in range(PUZZLE_SIZE):
        for i in range(PUZZLE_SIZE-1, -1, -1):
            new_puzzle[j][PUZZLE_SIZE-1-i] = puzzle[i][j]
    # for line in new_puzzle: print(line)
    # print()
    
    # 왼쪽 끝으로 붙이기
    while True:
        check = True
        for i in range(PUZZLE_SIZE):
            if new_puzzle[i][0] == 1:
                check = False; break
                
        if check:
            for i in range(PUZZLE_SIZE):
                for j in range(PUZZLE_SIZE-1):
                    new_puzzle[i][j] = new_puzzle[i][j+1]
            for i in range(PUZZLE_SIZE): new_puzzle[i][PUZZLE_SIZE-1] = 0
        else: break
    # for line in new_puzzle: print(line)
    # print()
    
    return new_puzzle

def solution(game_board, table):
    answer = 0
    
    N = len(table)
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    puzzles = [] # 퍼즐 조각들을 담아두는 리스트
    visited = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1: visited[i][j] = 0
    # for line in visited: print(line)
    
    # BFS로 퍼즐 리스트 생성
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: continue
            
            tmp_puzzle = []
            visited[i][j] = 1; que = deque([(i, j)]) # 큐에 현재 위치 넣고 시작
            
            # 퍼즐 찾기
            while que:
                x, y = que.popleft()
                tmp_puzzle.append((x, y))
                
                for d in range(4):
                    next_x, next_y = x+dx[d], y+dy[d]
                    if 0 <= next_x and next_x < N and 0 <= next_y and next_y < N:
                        if table[next_x][next_y] == 1 and visited[next_x][next_y] == 0: # 블록 위치이면서, 방문하지 않은 곳
                            visited[next_x][next_y] = 1
                            que.append((next_x, next_y))
            
            # 퍼즐 저장
            new_puzzle = [[0 for _ in range(PUZZLE_SIZE)] for _ in range(PUZZLE_SIZE)]
            min_x, min_y = tmp_puzzle[0]
            for x, y in tmp_puzzle:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
            for x, y in tmp_puzzle: new_puzzle[x-min_x][y-min_y] = 1
            # for line in new_puzzle: print(line)
            # print()
            puzzles.append(new_puzzle)
    
    # 퍼즐 맞는지 비교
    for puzzle in puzzles:
        tmp_puzzle = puzzle
        for _ in range(4):
            # 퍼즐 -> 위치 리스트
            pos_puzzle = []
            for i in range(PUZZLE_SIZE):
                for j in range(PUZZLE_SIZE):
                    if tmp_puzzle[i][j] == 1: pos_puzzle.append((i, j))
            # print(pos_puzzle)
            
            use_puzzle = False
            # game_board에서 퍼즐에 맞는 빈칸 찾기
            for i in range(N):
                for j in range(N):
                    check = True
                    
                    ## 1. 퍼즐이 board 밖에 나가는지 확인
                    for x, y in pos_puzzle:
                        if 0 > x+i or x+i >= N or 0 > y+j or y+j >= N:
                            check = False
                            break
                    if not check: check = True; continue
                    
                    ## 2. 퍼즐 빈칸에 넣을 수 있는지 확인
                    for x, y in pos_puzzle:
                        if game_board[x+i][y+j] == 1:
                            check = False
                            break
                    if not check: check = True; continue
                    
                    ## 3. 퍼즐이 그 빈칸에 딱 맞는지 확인
                    for x, y in pos_puzzle:
                        for d in range(4): # 상하좌우 확인
                            around_x, around_y = x+i+dx[d], y+j+dy[d]
                            if 0 <= around_x and around_x < N and 0 <= around_y and around_y < N:
                                if game_board[around_x][around_y] == 0: # 빈칸이 있다면?
                                    in_puzzle_check = True # 그 빈칸이 퍼즐로 채워질 빈칸인지 확인
                                    for px, py in pos_puzzle:
                                        if around_x == px+i and around_y == py+j:
                                            in_puzzle_check = False
                                            break
                                    if in_puzzle_check: check = False # 퍼즐로 채워지는 빈칸이 아닌 경우 -> 해당 위치의 퍼즐이 아니라는 뜻
                    if not check: check = True; continue
                                        
                    ## 4. check = True -> 즉, 해당 위치의 퍼즐을 찾음!
                    ## game_board에 퍼즐 넣고 answer에 추가
                    for x, y in pos_puzzle:
                        game_board[x+i][y+j] = 1
                    use_puzzle = True
                    answer += len(pos_puzzle)
                    break
                if use_puzzle: break
            
            # 회전 후 다시 판단
            if use_puzzle: break
            else: tmp_puzzle = rotate_90(tmp_puzzle)
    
    # for line in game_board: print(line)
    # print()
    
    return answer