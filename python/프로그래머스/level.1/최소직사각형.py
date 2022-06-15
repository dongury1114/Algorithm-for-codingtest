sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


max_w = 0
max_h = 0

for i in range(len(sizes)):
    sizes[i].sort(reverse=True)
    if sizes[i][0] > max_w:
        max_w = sizes[i][0]

    if sizes[i][1] > max_h:
        max_h = sizes[i][1]
print(max_w * max_h)

# -------------------------------------
for a, b in sizes:
    if a < b:
        a, b = b, a
    max_w = max(max_w, a)
    max_h = max(max_h, b)
print(max_w * max_h)
