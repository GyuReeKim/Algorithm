# 2068번
test = int(input())
for t in range(test):
    number = list(map(int, input().split()))
    max_num = 0
    for num in number:
        if num > max_num:
            max_num = num
    print('#{0} {1}'.format(t+1, max_num))