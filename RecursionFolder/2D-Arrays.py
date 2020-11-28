n = 8
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = "="
        elif i > j:
            a[i][j] = "*"
        else:
            a[i][j] = "-"
for row in a:
    print('= '.join([str(elem) for elem in row]))
print()

