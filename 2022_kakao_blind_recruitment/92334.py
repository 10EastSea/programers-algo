# 신고 결과 받기
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report_dict = defaultdict(set)   # 신고한 결과
    reported_dict = defaultdict(set) # 신고된 결과
    for content in report:
        a, b = content.split()
        report_dict[a].add(b)
        reported_dict[b].add(a)
    # print(report_dict)
    # print(reported_dict)
    
    for a in id_list:
        cnt = 0
        if a in report_dict:
            for b in report_dict[a]:
                if len(reported_dict[b]) >= k: cnt += 1
        answer.append(cnt)
    
    return answer