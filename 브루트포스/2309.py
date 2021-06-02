#https://www.acmicpc.net/problem/2309

def solution(height):
    height.sort()
    total = sum(height)
    for i in range(9):
        for j in range(i+1, 9):
            if total - (height[i]+height[j]) == 100:
                one = height[i]
                two = height[j]
    height.remove(one)
    height.remove(two)
    return height

height = []
for i in range(9):
    height.append(int(input()))

solution(height)
for n in height:
    print(n)
