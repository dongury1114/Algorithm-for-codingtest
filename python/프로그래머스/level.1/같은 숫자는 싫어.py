
tmp = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        tmp.append(arr[i])
print(tmp)

# ----------------------------
tmp = []
for i in arr:
    if tmp[-1:] == [i]:
        continue
    tmp.append(i)
print(tmp)
