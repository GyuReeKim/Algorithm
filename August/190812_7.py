# 2056번
test = int(input())
for t in range(test):
    date = input()
    day = ''
    for d in range(8):
        if d == 4 or d == 6:
            day = day + '/' + date[d]
        else:
            day += date[d]

    if 0 < int(day[5:7]) <= 12:
        if day[6] == '2':
            if 0 < int(day[8:]) < 29:
                print('#{0} {1}'.format(t+1, day))
            else:
                print('#{0} -1'.format(t+1))
        elif day[6] == '4' or day[6] == '6' or day[6] == '9' or day[6] == '11':
            if 0 < int(day[8:]) < 31:
                print('#{0} {1}'.format(t+1, day))
            else:
                print('#{0} -1'.format(t+1))
        else:
            if 0 < int(day[8:]) < 32:
                print('#{0} {1}'.format(t+1, day))
            else:
                print('#{0} -1'.format(t+1))
    else:
        print('#{0} -1'.format(t+1))