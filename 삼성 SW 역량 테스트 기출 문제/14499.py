#https://www.acmicpc.net/problem/14499
#주사위 굴리기
#memory:28776KB
#time:72ms

n,m,x,y,k = map(int, input().split()) #지도크기, 주사위현재좌표, 명령개수
graph = [list(map(int, input().split())) for _ in range(n)] #칸 정보 입력
orders = list(map(int, input().split())) #명령의 개수
dice = [0] * 7 #주사위

#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(k):
    order = int(orders.pop(0))
    nx = x + dx[order-1]
    ny = y + dy[order-1]

    if 0 <= nx < n and 0 <= ny < m: #맵 밖이 아니면
        if order == 1: #동쪽
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif order == 2: #서쪽
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif order == 3: #북쪽
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        else: #남쪽
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

        if graph[nx][ny] == 0:  # 해당칸이 0이면
            graph[nx][ny] = dice[6]  # 주사위의 값 복사
        else:  # 0이 아니면
            dice[6] = graph[nx][ny]  # 주사위에 칸 값 복사
            graph[nx][ny] = 0  # 칸 값은 0

        x = nx
        y = ny
        print(dice[1])
