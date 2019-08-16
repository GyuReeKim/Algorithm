T = int(input())
for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    arr = [[0]*N for n in range(N)]

    for i in range(N):
        chars = input()
        for j in range(N):
            arr[i][j] = chars[j]

    for i in range(N):
        row = ''
        col = ''
        for j in range(N):
            row += arr[i][j]
            col += arr[j][i]

        # print(row)
        for r in range(N-M+1):
            pal_r = row[r: r+M]
            if pal_r == pal_r[::-1]:
                print('#{} {}'.format(tc, pal_r))
                # break

        # print(col)
        for c in range(N-M+1):
            pal_c = col[c: c+M]
            if pal_c == pal_c[::-1]:
                print('#{} {}'.format(tc, pal_c))
                # break