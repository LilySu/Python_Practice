
def solution(T):
    sec = T % 60
    sec_c = T // 60
    min = sec_c % 60
    min_c = sec_c // 60
    hour = min_c % 60
    return f'{hour}h{min}m{sec}s'

if __name__=='__main__':
    T = 7500
    print(solution(3610))