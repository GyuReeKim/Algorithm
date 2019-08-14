# 색칠하기
arr = [[0]*10 for i in range(10)]
print(arr)

for i in range(10):
    for j in range(10):
        if 2 <= i <= 4 and 2 <= j <= 4:
            arr[i][j] = 1
        if 3 <= i <= 6 and 3 <= j <= 6:
            if arr[i][j] == 0:
                arr[i][j] = 2
            else:
                arr[i][j] += 2
print(arr)

count = 0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 3:
            count += 1
print(count)