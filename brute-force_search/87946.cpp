// 피로도

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int answer = -1;

void swap(int &a, int &b) {
    int tmp = b;
    b = a;
    a = tmp;
}

void permutations(int *idx_list, int depth, int n, int k, vector<vector<int>> dungeons) {
    if(depth == n) { // 조합 생성
        int tmp_answer = 0; int tmp_k = k;
        for(int i=0; i<n; i++) {
            // cout << idx_list[i] << " ";
            if(tmp_k >= dungeons[idx_list[i]][0]) { tmp_k -= dungeons[idx_list[i]][1]; tmp_answer += 1; }
        }
        // cout << "/ " << tmp_answer << endl;
        if(answer < tmp_answer) answer = tmp_answer;
    }
    
    for(int i=depth; i<n; i++) {
        swap(idx_list[depth], idx_list[i]);
        permutations(idx_list, depth+1, n, k, dungeons);
        swap(idx_list[depth], idx_list[i]);
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    int *idx_list = new int[dungeons.size()];
    for(int i=0; i<dungeons.size(); i++) idx_list[i] = i;
    
    permutations(idx_list, 0, dungeons.size(), k, dungeons);
    
    return answer;
}