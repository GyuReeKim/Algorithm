# 2070번
test = int(input())
for t in range(test):
    a, b = list(map(int, input().split()))
    if a > b:
        print('#{0} >'.format(t+1))
    elif a < b:
        print('#{0} <'.format(t+1))
    else:
        print('#{0} ='.format(t+1))