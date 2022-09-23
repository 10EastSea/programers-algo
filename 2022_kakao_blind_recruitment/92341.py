# 주차 요금 계산
from collections import defaultdict
import math

def time_calc(start, end):
    start_h, start_m = list(map(int, start.split(':')))
    end_h, end_m = list(map(int, end.split(':')))
    start_m += start_h*60; end_m += end_h*60
    return end_m - start_m

def solution(fees, records):
    answer = []
    
    car_dict = defaultdict(list)
    for record in records:
        time, car, state = record.split()
        car_dict[car].append((state, time))
    # print(car_dict)
    
    car_list = []
    for car, record in car_dict.items():
        if len(record) % 2 != 0: record.append(('OUT', '23:59'))
        car_list.append(car)
        
        total_time = 0
        for i in range(0, len(record), 2):
            total_time += time_calc(record[i][1], record[i+1][1])
        # print(total_time)
        
        if fees[0] >= total_time: car_dict[car] = fees[1]
        else: car_dict[car] = fees[1] + (math.ceil((total_time-fees[0]) / fees[2]) * fees[3])
    # print(car_dict)
    
    car_list.sort()
    for car in car_list: answer.append(car_dict[car])
    
    return answer