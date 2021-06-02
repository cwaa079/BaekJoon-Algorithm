#https://www.acmicpc.net/problem/1476

#내가 푼 코드
def solution(e,s,m):
    cnt, ne, ns, nm = 0, 0, 0, 0
    while True:
        cnt += 1; ne += 1; ns += 1; nm += 1
        if ne % 16 == 0: ne = 1     
        if ns % 29 == 0: ns = 1
        if nm % 20 == 0: nm = 1
        if ne == e and ns == s and nm == m: break
    return cnt

e, s, m = map(int, input().split())
print(solution(e,s,m))


#다른 사람 참고 코드
def solution(e,s,m):
  year = 0
  while True:
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        break
    year += 1
  return year
