# 전기버스
# 다시풀어보기
# K, N, M = list(map(int, input().split()))
# energy = list(map(int, input().split()))
K = 5
N = 20
M = 5
energy = [4, 7, 9, 14, 17]
stop = [0] * (N+1)
bus_stop = []
for n in range(N+1):
    if n in energy:
        stop[n] = 1
        bus_stop.append(n)
    elif n == 0 or n == N:
        stop[n] = 1
        bus_stop.append(n)
print(bus_stop)
            
