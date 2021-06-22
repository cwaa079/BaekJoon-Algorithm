#https://www.acmicpc.net/problem/6064
#카잉달력

"""
처음 푼 코드
이 문제의 시간복잡도는 O(M*N)이므로 
해당 코드는 10^10이므로 시간초과이다.
"""
def solution(m, n, x, y):
    nx, ny = 1, 1
    for i in range(1, 40001):

        if nx == x and ny == y:
            return i

        if nx < m: nx += 1
        else: nx = 1

        if ny < n: ny += 1
        else: ny = 1

    return -1

"""
인터넷 풀이 코드
따라서 백트래킹으로 조건에 맞는 것만 검사하는 알고리즘이 필요하다.
"""
def solution(m, n, x, y):
    for i in range(x, m*n+1, m):
        if i % n == y % n:
            return i
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(solution(m, n, x, y))
