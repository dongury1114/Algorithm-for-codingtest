def solution(cacheSize, cities):

    stack = []
    time = 0
    tmp = []
    for i in cities:
        tmp.append(i.upper())
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in tmp:
            if not i in stack:
                if len(stack) < cacheSize:
                    stack.append(i)
                    time += 5

                else:
                    stack.pop(0)
                    stack.append(i)
                    time += 5
            else:
                stack.pop(stack.index(i))
                stack.append(i)
                time += 1

        return time
