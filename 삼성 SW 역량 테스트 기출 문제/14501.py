#https://www.acmicpc.net/problem/14501
#퇴사 (dp문제)
#memory:28776KB
#time:64ms

n = int(input()) #남은날짜
t = [0] * n#걸리는 기간
p = [0] * n #금액
dp = [0] * (n+1)

#정보 입력
for i in range(n):
    t[i], p[i] = map(int, input().split())
    dp[i] = p[i]
dp[n] = 0 #마지막은 0초기화

for i in range(n-1, -1, -1):
    if t[i] + i > n: #남은 일수보다 걸리는 기간이 크면
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[t[i]+i])
print(dp[0])
