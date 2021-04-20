#https://www.acmicpc.net/problem/3687
#성냥개비
#dp(점화식 잘 세우기), 오버

import sys
INF = sys.maxsize * sys.maxsize

n = int(input()) #성냥개비 개수
min_dp = [INF] * 101

def max_num(num): #가장 큰수를 찾아서 리턴
    temp = ""
    if num % 2 == 0:
        for i in range(num//2):
            temp += "1"
    else:
        temp += "7"
        for i in range((num-3)//2):
            temp += "1"
    return temp

def min_num(): #dp
    minlist = ["1", "7", "4", "2", "0", "8"]  # 반복되는 숫자

    min_dp[2], min_dp[3], min_dp[4], min_dp[5] = "1", "7", "4", "2"
    min_dp[6], min_dp[7], min_dp[8] = "6", "8", "10"

    for i in range(9, 101):
        for j in range(2, 8):
            temp = min_dp[i-j] + minlist[j-2]
            min_dp[i] = str(min(int(min_dp[i]), int(temp)))

min_num()
for i in range(n):
    num = int(input()) #현재 수
    print(min_dp[num], max_num(num))
