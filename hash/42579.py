# 베스트앨범
from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    
    genres_dict = defaultdict(list)
    for i in range(len(genres)):
        heapq.heappush(genres_dict[genres[i]], (-plays[i], i))
    # print(genres_dict)
    
    # 인기 장르 찾기
    top_genre = []
    for genre in genres_dict.keys():
        sum = 0
        for music in genres_dict[genre]: sum += music[0]
        heapq.heappush(top_genre, (sum, genre))
    # print(top_genre)
    
    # 인기 장르에서 부터 두개씩 추가
    while top_genre:
        music = heapq.heappop(top_genre)
        genre = music[1] # 장르 저장
        
        tmp_answer = []
        for _ in range(2): # 2번 반복
            if genres_dict[genre]:
                music = heapq.heappop(genres_dict[genre])
                tmp_answer.append(music[1]) # index 저장
        answer.extend(tmp_answer)
    
    return answer