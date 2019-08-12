# 2063번
odd_num = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
for n in range(odd_num):
    if n == odd_num // 2:
        print(numbers[n])