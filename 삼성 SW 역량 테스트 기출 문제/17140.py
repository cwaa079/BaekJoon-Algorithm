#https://www.acmicpc.net/problem/17140
#이차원 배열과 연산
#transpose와 Counter 이용

from collections import Counter
r, c, k = map(int, input().split()) #행열,값
ary = [list(map(int, input().split())) for _ in range(3)]

def R():
    max_len = 0
    len_ary = len(ary)
    for j in range(len_ary):
        temp = [i for i in ary[j] if i != 0]
        temp = Counter(temp).most_common() #[('1',3개),]
        temp.sort(key=lambda x: (x[1], x[0])) #개수를 기준으로 정렬
        ary[j] = [] #초기화
        for first, second in temp:
            ary[j].append(first) #숫자
            ary[j].append(second) #개수
        len_temp = len(temp)
        if max_len < len_temp*2: #temp의 원소1개는 ary의 2개이므로
            max_len = len_temp*2

    #최대개수만큼 세서 0으로 채워주기
    for j in range(len_ary):
        for k in range(max_len - len(ary[j])):
            ary[j].append(0)
        ary[j] = ary[j][:100] #100개가 넘어가면 처음 100개를 제외한 나머지 버림

t = 0 #걸린 시간
while(True):
    if t > 100:
        print(-1)
        break
    if r-1 < len(ary) and c-1 < len(ary[0]): #기준보다 커야함
        if ary[r-1][c-1] == k:
            print(t)
            break
    if len(ary) >= len(ary[0]): # 행 >= 열이면 R연산
        R()
    else: #C연산
        ary = list(map(list, zip(*ary)))
        R()
        ary = list(map(list, zip(*ary)))
    t += 1
