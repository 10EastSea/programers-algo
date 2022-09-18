// 게임 맵 최단거리

#include <vector>
// #include <iostream>
using namespace std;

class Point {
public:
    int x; int y;
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

int solution(vector<vector<int>> maps)
{
    int answer = 1;
    
    int dx[] = {-1, 0, 1, 0};
    int dy[] = {0, 1, 0, -1};
    int n = maps.size(); int m = maps[0].size();
    
    Point start = Point(0, 0, 1); Point end = Point(n-1, m-1, -1); // 시작점, 도착점 선언
    vector<Point> queue; queue.push_back(start); // 큐에 시작점 넣고 시작
    
    int **visited = new int*[n]; for(int i=0; i<n; i++) visited[i] = new int[m]; // 방문 기록
    for(int i=0; i<n; i++) { for(int j=0; j<m; j++) { visited[i][j] = 0; } } visited[start.x][start.y] = 1; // 방문 기록 초기화
    
    // BFS
    while(queue.size() != 0) { // 갈 수 있는 길이 없을 때
        Point here = queue.front(); queue.erase(queue.begin());
        // cout << here.move_cnt << " (" << here.x << ", " << here.y << ")" << endl;
        
        if(is_equal(here, end) == 1) { // 도착했을 때
            answer = here.move_cnt;
            break;
        }
        
        for(int i=0; i<4; i++) { // 다음으로 이동
            int next_x = here.x + dx[i]; int next_y = here.y + dy[i];
            if(0 <= next_x && next_x < n && 0 <= next_y && next_y < m) {
                if(maps[next_x][next_y] == 1 && visited[next_x][next_y] == 0) { // 이동할 수 있는 길이면서, 방문하지 않은 길
                    visited[next_x][next_y] = 1;
                    queue.push_back(Point(next_x, next_y, here.move_cnt+1));
                }
            }
        }
        
        if(queue.size() == 0) { // 도착 못했을 때
            answer = -1;
            break;
        }
    }
    
    return answer;
}