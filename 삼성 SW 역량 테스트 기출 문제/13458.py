#https://www.acmicpc.net/problem/13458
#시험감독
#memory:148224KB
#time : 916ms

n = int(input()) #시험장 개수
a = list(map(int, input().split())) #응시자 수
b, c = map(int, input().split()) #총감독관, 부감독관 감독

totalCnt = n
elseCnt = 0
for i in range(n):
    if a[i] > 0:
        a[i] -= b

    if a[i] > 0:
        elseCnt += a[i] // c
        if a[i] % c > 0:
            elseCnt += 1

print(totalCnt+elseCnt)
