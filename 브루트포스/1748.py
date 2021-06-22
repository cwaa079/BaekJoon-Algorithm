#https://www.acmicpc.net/problem/1748
#수 이어 쓰기1

"""
처음에 알고리즘을 생각하길
리스트에 n까지 str형으로 할당한 다음 len으로 길이를 세줄려고 했으나
문제에서 주어진 입력 조건 때문에 메모리할당 & 시간 초과 발생

따라서 자릿수에 따른 개수를 이용하여 로직을 세워야 함.
"""

n = int(input())
lines = [int('9'+'0' * i) for i in range(len(str(n)))] #[9, 90, 900 ...]
result = 0

for i, s in enumerate(lines):
    if s == lines[-1]: #마지막 자릿수라면
        result += len(str(s)) * (n - sum(lines[:-1]))
    else:
        i += 1
        result += i * s

print(result)

