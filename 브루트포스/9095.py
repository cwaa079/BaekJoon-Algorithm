#https://www.acmicpc.net/problem/9095
#DP문제 - 규칙 파악하기
def solution(num):
    dp = [1, 2, 4]
    for i in range(3, num):
      dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    return dp[num-1]


n = int(input())
for i in range(n):
  num = int(input())
  print(solution(num))
