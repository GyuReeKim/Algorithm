# 전기버스
T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # bus_stop = [0] + list(map(int, input().split())) + [N]
    energy = list(map(int, input().split()))
    stop = [0] * (N+1)
    bus_stop = []
    for n in range(N+1):
        if n in energy:
            stop[n] = 1
            bus_stop.append(n)
        elif n == 0 or n == N:
            stop[n] = 1
            bus_stop.append(n)
    # print(bus_stop)

    last = bus_stop[0]
    count = 0

    for i in range(1, len(bus_stop)):
        if bus_stop[i] - bus_stop[i-1] > K:
            count = 0
            break
        elif bus_stop[i] - last > K:
            count += 1
            last = bus_stop[i-1]

    print('#{} {}'.format(tc, count))