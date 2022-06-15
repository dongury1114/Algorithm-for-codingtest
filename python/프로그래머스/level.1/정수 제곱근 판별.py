import math

n = 3

tmp = int(math.sqrt(n))  # n ** 1/2
ans = pow(tmp + 1, 2)
if pow(tmp, 2) != n:
    print(-1)
else:
    print(ans)
