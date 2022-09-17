// 전력망을 둘로 나누기

#include <string>
#include <vector>
// #include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    
    for(int cnt=0; cnt<wires.size(); cnt++) {
        // 송전탑 연결 정보
        int *nodes = new int[n+1];
        for(int i=0; i<=n; i++) nodes[i] = i;
        
        // wires 중 하나 뺐을 때, 연결 상태 업데이트
        for(int i=0; i<wires.size(); i++) {
            if(cnt == i) continue;
            
            int left = nodes[wires[i][0]]; int right = nodes[wires[i][1]];
            int parent = left > right ? right : left;
            int child = left > right ? left : right;
            
            // 바뀐 부모 업데이트
            nodes[child] = parent; nodes[wires[i][0]] = parent; nodes[wires[i][1]] = parent;
            for(int j=1; j<=n; j++) {
                if(nodes[j] == child || nodes[j] == wires[i][0] || nodes[j] == wires[i][1]) nodes[j] = parent;
            }
        }
        
        // 송전탑 개수 세기
        int tower1 = 0; int tower2 = 0;
        int cnt1 = 0; int cnt2 = 0;
        for(int i=1; i<=n; i++) {
            // cout << nodes[i] << " ";
            if(tower1 == 0) { tower1 = nodes[i]; cnt1++; }
            else if(tower1 == nodes[i]) { cnt1++; }
            else if(tower2 == 0) { tower2 = nodes[i]; cnt2++; }
            else { cnt2++; }
        }
        // cout << endl;
        
        // cout << cnt1 << ", " << cnt2 << endl;
        int tmp_answer = cnt1 >= cnt2 ? cnt1-cnt2 : cnt2-cnt1;
        if(answer > tmp_answer) answer = tmp_answer;
        
        delete nodes;
    }
    
    return answer;
}