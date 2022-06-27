# 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    num = len(jobs)
    
    time = 0
    heapq.heapify(jobs)
    while jobs:
        current_process = heapq.heappop(jobs)
        time = current_process[0] + current_process[1]
        answer += current_process[1]

        ## 스케줄러 만드는 과정 (반복) ##
        if not jobs: break # 남아있는 job이 없다면 stop
        tmp_process = heapq.heappop(jobs)
        scheduler = [tmp_process]
        while time >= tmp_process[0]:
            if not jobs: break
            tmp_process = heapq.heappop(jobs)
            scheduler.append(tmp_process)
        tmp_process = scheduler.pop() # 맨 마지막 job 확인
        if time >= tmp_process[0]: scheduler.append(tmp_process)
        else: heapq.heappush(jobs, tmp_process)

        ## 스케줄러 정렬하는 과정 (반복) ##
        scheduler = list(map(lambda l: [l[1],l[0]], scheduler))
        heapq.heapify(scheduler) # 스케줄 시간 순으로 정렬

        while scheduler:
            current_process = heapq.heappop(scheduler)
            time += current_process[0]
            answer += (time - current_process[1])

            ## tmp스케줄러 만드는 과정 (반복) ##
            if not jobs: continue # 남아있는 job이 없다면 그냥 진행
            tmp_process = heapq.heappop(jobs)
            tmp_scheduler = [tmp_process]
            while time >= tmp_process[0]:
                if not jobs: break
                tmp_process = heapq.heappop(jobs)
                tmp_scheduler.append(tmp_process)
            tmp_process = tmp_scheduler.pop() # 맨 마지막 job 확인
            if time >= tmp_process[0]: tmp_scheduler.append(tmp_process)
            else: heapq.heappush(jobs, tmp_process)

            ## tmp스케줄러와 스케줄러 합치고, 스케줄러 정렬하는 과정 (반복) ##
            tmp_scheduler = list(map(lambda l: [l[1],l[0]], tmp_scheduler))
            scheduler.extend(tmp_scheduler)
            heapq.heapify(scheduler) # 스케줄 시간 순으로 정렬
            
    answer = int(answer/num)
    return answer