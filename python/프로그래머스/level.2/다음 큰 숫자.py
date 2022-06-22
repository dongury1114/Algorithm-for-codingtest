# 78(1001110)
# 83(1010011)
# 15(1111)
# 23(10111)

# 끝이 0 인 경우 1로 바꾸기
# 전부 1 인 경우 맨앞의 1 뒤에 0 넣기
# 끝이 0 이아닌경우
#

# n = 78
n = 15
n = bin(n)
n = list(n)[2:]
if n[-1] == "0":
    n[-1] = "1"
elif "0" not in n:
    n.insert(1, "0")
ans = "0b"+"".join(n)
print(int(ans, 2))
# print(ans)
# print(n)
