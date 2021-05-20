#https://www.acmicpc.net/problem/1149
#dp문제

def solution(n, rgb):
    for i in range(1, len(rgb)):
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
        rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
        rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

    return min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2])

n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

print(solution(n, rgb))
