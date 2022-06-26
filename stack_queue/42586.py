# 기능개발
def solution(progresses, speeds):
    answer = []

    day = 0
    while progresses:
        day += 1
        
        progress = progresses[0]
        if progress + (speeds[0] * day) < 100: continue

        progresses.pop(0)
        speeds.pop(0)
        finish = 1

        while progresses:
            progress = progresses[0]
            if progress + (speeds[0] * day) < 100: break

            progresses.pop(0)
            speeds.pop(0)
            finish += 1
        
        answer.append(finish)

    return answer