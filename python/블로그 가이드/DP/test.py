import re
from collections import defaultdict

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

arr = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
arr = list(arr.split())
# graph = defaultdict(int)
graph = dict()
banned = list(map(lambda x: x.lower(), banned))
# print(arr)
print(graph)
for i in arr:
    i = i.lower()
    if not i in banned:
        if i in graph.keys():
            graph[i] += 1
        else :
            graph[i] = 1

# print(graph)

# max = 0
# result = ''

# for k, v in graph.items():
#     if v > max :
#         max = v
#         result = k
# print(result)