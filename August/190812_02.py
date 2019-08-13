# 2071번
test = int(input())
for t in range(test):
    number = list(map(int, input().split()))
    result = 0
    for num in number:
        result += num

    average = round(result/len(number))
    print('#{0} {1}'.format(t+1, average))