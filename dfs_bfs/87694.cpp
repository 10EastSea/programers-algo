// 아이템 줍기

#include <string>
#include <vector>
// #include <iostream>

#define MAP_SIZE 100*2
using namespace std;

class Point {
public:
    int x, y;
    int move_cnt;
    Point(int x, int y, int move_cnt) {
        this->x = x; this->y = y;
        this->move_cnt = move_cnt;
    }
};

int is_equal(Point p1, Point p2) {
    if(p1.x == p2.x && p1.y == p2.y) return 1;
    return 0;
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
    
    // map 초기화
    int **map = new int*[MAP_SIZE]; for(int i=0; i<MAP_SIZE; i++) { map[i] = new int[MAP_SIZE]; }
    for(int i=0; i<MAP_SIZE; i++) { for(int j=0; j<MAP_SIZE; j++) { map[i][j] = 1; } } // 다 1로 세팅
    for(int r=0; r<rectangle.size(); r++) { // 2칸씩 띄어서 그리기
        int start_x = rectangle[r][0]*2, start_y = rectangle[r][1]*2, end_x = rectangle[r][2]*2, end_y = rectangle[r][3]*2;
        
        for(int x=start_x; x<=end_x; x++) {
            if(map[x][start_y] != 2) map[x][start_y] = 0;
            if(map[x][end_y] != 2) map[x][end_y] = 0;
        }
        for(int y=start_y; y<=end_y; y++) {
            if(map[start_x][y] != 2) map[start_x][y] = 0;
            if(map[end_x][y] != 2) map[end_x][y] = 0;
        }
        
        for(int x=start_x+1; x<end_x; x++) { // 사각형 내부 색칠하기
            for(int y=start_y+1; y<end_y; y++) map[x][y] = 2;
        }
    }
    // for(int i=0; i<MAP_SIZE; i++) { for(int j=0; j<MAP_SIZE; j++) { cout << map[i][j] << " "; } cout << endl; }
    
    // visited 초기화
    int **visited = new int*[MAP_SIZE]; for(int i=0; i<MAP_SIZE; i++) { visited[i] = new int[MAP_SIZE]; }
    for(int i=0; i<MAP_SIZE; i++) { for(int j=0; j<MAP_SIZE; j++) { visited[i][j] = 0; } }
    
    Point start = Point(characterX*2, characterY*2, 0), end = Point(itemX*2, itemY*2, -1);
    visited[start.x][start.y] = 1;
    vector<Point> que; que.push_back(start);
    
    // BFS
    while(que.size() != 0) {
        Point here = que.front(); que.erase(que.begin());
        if(here.x == end.x && here.y == end.y) { answer = here.move_cnt; break; } // 도착했을 때
        
        for(int i=0; i<4; i++) {
            int check_x = here.x+dx[i], check_y = here.y+dy[i], next_x = here.x+dx[i]*2, next_y = here.y+dy[i]*2;
            if(0 <= next_x && next_x < MAP_SIZE && 0 <= next_y && next_y < MAP_SIZE) {
                if(map[check_x][check_y] == 0 && visited[next_x][next_y] == 0) { // 이동할 수 있는 길이면서, 방문하지 않은 길
                    visited[next_x][next_y] = 1;
                    que.push_back(Point(next_x, next_y, here.move_cnt+1));
                }
            }
        }
    }
    
    return answer;
}