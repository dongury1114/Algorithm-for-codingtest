arr1, arr2 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
# arr1, arr2 = [[1], [2]], [[3], [4]]

# sol.2
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        arr1[i][j] += arr2[i][j]
print(arr1)

# sol.1 내풀이
# ans = []
# for i in range((len(arr1))):
#     tmp = []
#     for j in range((len(arr1[0]))):
#         tmp.append(arr1[i][j] + arr2[i][j])
#     ans.append(tmp)
# print(ans)
