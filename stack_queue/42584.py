# 주식가격
def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
    for idx, price in enumerate(prices):
        while stack:
            if stack[len(stack)-1][0] > price: # 빼내야 함
                _, s, i = stack.pop()
                answer[i] = s
            else: break
        stack.append((price, 0, idx))
        
        stack = list(map(lambda x: (x[0], x[1]+1, x[2]), stack))
    
    while stack:
        _, s, i = stack.pop()
        answer[i] = s-1
    
    return answer