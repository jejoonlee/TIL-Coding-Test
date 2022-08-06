import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    # 세 변의 수는 항상 주어지기 때문에 입력 값으로 넣는다
    # a, b, c = map(int, input().split())
    # 세 변의 수가 같으면 무조건 정사각형이다

    # 따라서 나머지 변의 길이도 같다
    # if a == b == c:
    #     print(f'#{t} {a}')
    # # a 와 b가 같으면 나머지 변의 길이는 c
    # elif a == b:
    #     print(f'#{t} {c}')
    # # a와 c가 같으면 나aj지 변의 길이는 b
    # elif a == c:
    #     print(f'#{t} {b}')
    # # b와 c가 같으면 나머지 변의 길이는 a
    # elif b == c:
    #     print(f'#{t} {a}')

    # 같은 길이의 변의 개수가 몇 개 주어졌는지 활용 (.count())?
    
    side = list(map(int, input().split()))

    dic = {}

    for i in side:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for key, value in dic.items():
        if value != 2:
            print(f'{t} {key}')