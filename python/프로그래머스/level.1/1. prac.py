answers = [1, 3, 2, 4, 2]
pattern1 = [1, 2, 3, 4, 5]
pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
score = [0, 0, 0]
result = []

for i, answer in enumerate(answers):
    if answer == pattern1[i % 5]:
        score[0] += 1
    if answer == pattern1[i % 8]:
        score[1] += 1
    if answer == pattern1[i % 10]:
        score[2] += 1

for i, s in enumerate(score):
    if s == max(score):
        result.append(i+1)
        # for idx, s in enumerate(score):
        #     if s == max(score):
        #         result.append(idx+1)
print(result)
