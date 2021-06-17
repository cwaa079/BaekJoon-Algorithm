#https://www.acmicpc.net/problem/1107
#아이디어가 중요함
#모든 경우의 수를 고려하기

def solution(n, m):

    remote_controller = {str(i) for i in range(10)} #문자열로 처리
    if m > 0: #없는 번호 제거
        remote_controller -= set(map(str, input().split()))

    now = 100 #현재 채널
    min_cnt = abs(now - n)

    for channel in range(1000000):
        for j in range(len(str(channel))):
            if str(channel)[j] not in remote_controller: break
            elif len(str(channel)) - 1 == j:
                min_cnt = min(min_cnt, abs(channel - n) + len(str(channel)))

    return min_cnt

n = int(input())
m = int(input())

print(solution(n, m))
