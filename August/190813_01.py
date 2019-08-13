# 구간합
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) 
    v = list(map(int, input().split()))
    A = []
    for n in range(M-1, N):
        v_small = v[n-M+1: n+1]
        # for m in range(0, n-M+2):
        #     v_small = v[m: m+M]
        # print(v_small)
        v_num = 0
        for v_n in v_small:
            v_num += v_n
        # print(v_num)
        A.append(v_num)
    # print(A)

    for mn in range(N-M, 0, -1):
        for a in range(0, mn):
            if A[a] >= A[a+1]:
                temp = A[a]
                A[a] = A[a+1]
                A[a+1] = temp
    min_A = A[0]
    max_A = A[-1]

    result = max_A - min_A
    print('#{} {}'.format(tc, result))