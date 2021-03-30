#https://www.acmicpc.net/problem/3190
#뱀
#memory : 28779
#time : 72ms

n = int(input()) #보드크기
k = int(input()) #사과개수
data = [[0]*(n+1) for _ in range(n+1)] #맵정보
di_info=[] #방향변환정보

#맵에 사과 입력
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input()) #방향 변환 횟수
for _ in range(l):
    x, c = input().split()
    di_info.append( (int(x), c) ) #(시간, 방향)

#동남서북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def simulate():
    x, y = 1, 1 #뱀의 첫 위치
    data[x][y] = 2 #뱀이 존재하는 위치
    di = 0 #방향 : 오른쪽
    q = [(x, y)] #현재 뱀의 위치
    index = 0 #다음에 회전할 정보
    time = 0 #시간
    while True:
        nx = x + dx[di]
        ny = y + dy[di]
        #맵 안에 있고 몸통이 머리와 만나지 않는다면
        if nx > 0 and nx <= n and ny > 0 and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0: #사과가 없으면
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1: #사과가 있으면
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny
        if index < l and time == di_info[index][0]: #회전할 시간
            if di_info[index][1] == "L": #왼쪽
                di = (di-1) % 4
            else:
                di = (di+1) % 4
            index += 1
    return time

print(simulate())
