# Flatten (평탄화)
Test = 10
for tc in range(Test):
    dump = int(input())
    box = list(map(int, input().split()))
    max_box = 0
    min_box = 0

    for d in range(dump):
        for i in range(len(box)):
            if box[max_box] < box[i]:
                max_box = i
            if box[min_box] > box[i]:
                min_box = i
        
        if box[max_box] - box[min_box] > 1:
            box[max_box] -= 1
            box[min_box] += 1

        else:
            print(box[max_box] - box[min_box])
            break

    # max_box와 min_box의 index를 반영해주기 위해 for문을 한번 더 써준다.
    for i in range(len(box)):
        if box[max_box] < box[i]:
            max_box = i
        if box[min_box] > box[i]:
            min_box = i
    print('#{} {}'.format(tc+1, box[max_box] - box[min_box]))