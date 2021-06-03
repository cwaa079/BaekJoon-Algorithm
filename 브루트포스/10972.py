#https://www.acmicpc.net/problem/10972
"""
순열과 정렬을 통해 풀었으나 메모리초과
"""
from itertools import permutations
def solution(n, num):
    temp = list(permutations(num, n))
    temp.sort()
    idx = 0
    for now in temp:
        if list(now) == num:
            if idx == len(temp)-1: return -1
            else: return ' '.join(map(str, temp[idx+1]))
        idx += 1

n = int(input())
num = list(map(int, input().split()))
print(solution(n, num))


"""
next_permutations 알고리즘 사용
"""
def solution(n, num):
    i, j = n-1, n-1
    while i>0 and num[i-1]>=num[i]:
        i -= 1
    if i==0: return -1

    while num[i-1]>=num[j]:
        j-=1
    num[i-1], num[j] = num[j], num[i-1]

    k = n-1
    while i < k:
        num[i], num[k] = num[k], num[i]
        i+=1; k-=1
    return ' '.join(map(str, num))


n = int(input())
num = list(map(int, input().split()))
print(solution(n, num))
