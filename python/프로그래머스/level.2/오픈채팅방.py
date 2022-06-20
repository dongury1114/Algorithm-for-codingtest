record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


#ans = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

ans = []
actions = []
userDB = dict()

for event in record:
    info = event.split()
    action, userid = info[0], info[1]
    actions.append((action, userid))
    if action == "Enter" or action == "Change":
        nickname = info[2]
        userDB[userid] = nickname

# for event in record:
#     info = event.split()
#     action, userid = info[0], info[1]
#     actions.append((action, userid))
#     if action == "Enter" or action == "Change":
#         nickname = info[2]
#         userDB[userid] = nickname


# print("ACT", actions)
# print("USER", userDB)

for actionInfo in actions:
    action, userid = actionInfo[0], actionInfo[1]
    if action == "Enter":
        ans.append(f'{userDB[userid]}님이 들어왔습니다.')
    elif action == "Leave":
        ans.append(f'{userDB[userid]}님이 나갔습니다.')

print(ans)
# for i in range(len(record)):
#     tmp.append(list(record[i].split()))

# for i in range(len(tmp)):
#     if tmp[i][0] == "Enter":
#         result.append([tmp[i][1], tmp[i][2]])
#         ans.append("{tmp[i][2]}님이 들어왔습니다.")
#     elif tmp[i][0] == "Leave":
#         for j in range(len(result)):
#             if result[j][0] == tmp[i][1]:
#                 123
# print(ans)
