# 2072번
test = int(input())
for t in range(test):
    number = list(map(int, input().split()))
    result = 0
    for num in number:
        if num % 2:
            result += num
    print('#{0} {1}'.format(t+1, result))