import sys

from collections import deque

sys.stdin = open("input.txt")
# 행번호, 방향 0 오른쪽 1 왼쪽, 회전수
# 출력: 362
n = int(input())

gom = list(list(map(int, input().split()))for _ in range(n))
m = int(input())

a = n//2
ans = 0
for i in range(m):
    row, direction, num = map(int, input().split())
    tmp = deque(gom[row-1])
    if direction == 0:
        tmp.rotate(-num)
    elif direction == 1:
        tmp.rotate(num)
    gom[row-1] = list(tmp)

for i in range(0, n):
    tmp = []
    if a > i:
        tmp = gom[i]
        ans += sum(tmp[i:n-i])
    elif a == i:
        ans += gom[i][a]
    elif a < i:
        tmp = gom[i]
        ans += sum(tmp[n-i-1:i+1])
print(ans)

# result = [27, 29, 37, 13, 19, 19, 13, 39]
# print(sum(result))
# 생각하기 쉽게 do 에 있는 행 지시 -1 씩
# 세팅완료
# 회전은 rotate 활용하자

# # 회전하기
# for i in range(m):
#     row, direction, num=map(int, input().split())  # 회전할 행, 방향, 칸 수 입력 받음
#     now=deque(mat[row-1])  # 회전할 행을 데크로 만듦
#     if direction == 0:  # 방향이 0이면 왼쪽으로 칸 수 만큼 회전
#         now.rotate(-num)
#     else:  # 방향이 1이면 오른쪽으로 칸 수 만큼 회전
#         now.rotate(num)
#     mat[row-1]=list(now)  # 배열에 반영
