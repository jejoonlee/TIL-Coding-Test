# 📋 Project 1

[1204 최빈수 구하기](#1204-최빈수-구하기)

[1288 암호문](#1288-암호문)

[3456 직사각형 길이찾기](#3456-직사각형-길이찾기)

[10505 소득 불균형](#10505-소득-불균형)

[10804 문자열의 거울상](#10804-문자열의-거울상)

[14649 신용카드 만들기 1](#14649-신용카드-만들기-1)

[14654 신용카드 만들기 2](#14654-신용카드-만들기-2)



### 1204 최빈수 구하기

> 딕셔너리를 활용했다.
>
> 점수들을 key로 넣고, 같은 점수가 있으면, value를 1씩 더했다.
>
> 그리고 value들 중, 제일 큰 value를 찾았다.
>
> 그리고 value를 통해 key를 찾아내고, key가 하나면 바로 출력을 하고, 2개 이상이면, max를 통해 제일 큰 값을 출력했다

```python
T = int(input())

for t in range(1, T + 1):
    t_num = int(input())
    inp_score = input().split()

    scores = {}
    # 딕셔너리에 점수를 넣는다. 
    # 점수가 key, 점수의 개수가 value
    for i in inp_score:
        if i in scores:
        # 점수가 이미 있으면, value에 1씩 더하기
            scores[i] += 1
        else:
        # 없으면 key를 넣고, 1을 설정
            scores[i] = 1
    
    # 딕셔너리 value 중에 제일 큰 숫자 가지고 오기
    max_val = max(scores.values())

    # max-val 이랑 숫자가 같은 key를 lst에 넣기
    lst = []
    for key, value in scores.items():
        if value == max_val:
            lst.append(key)
    
    result = list(map(int, lst))
    
    # 리스트 안에서 max 숫자를 가지고 오면, 답이 된다
    print(f'#{t_num} {max(result)}')
```



### 1288 암호문

> .insert를 사용하기

```python
for t in range(1, 11):

    ori_range = int(input())
    # 원본 암호문 길이

    ori = list(input().split())
    # 원본 암호문

    com_range = int(input())
    # 명령어의 개수

    com = input().split()
    # 명령어

    i = 0

    # 명령어가 끝날때까지 i를 돌린다
    while i < len(com):
        command = com[i]
        # 명령어를 순회하며 I가 있으면, 그 뒤의 숫자들을
        # 저장한다.
        # 원본 x 번째에 넣어야 하고
        # 원본에 넣아야 할 숫자들의 개수는 y개고
        # ad는 원본에 넣어야 할 숫자들이다
        if command == 'I':
            x = int(com[i + 1])
            y = int(com[i + 2])
            ad = com[i + 3 : i + y + 3]

            # 한번에 슬라이싱 한 ad 를 원본에 못 넣는다
            for a in ad[::-1]:
                ori.insert(x, a)

        i += 1

    result = ori[:10]

    print(f'#{t}', *result)
```

#### 🚨🚨🚨 중요 🚨🚨🚨 

- while문을 사용해서 순회를 한다.
  - 여기서는 명령어의 길이를 한번 순회하면, while문이 끝난다
- `.insert(x, a)` 를 통해서 숫자들을 슬라이싱 한 `ad` 를 하나씩 꺼내서, 원본에 넣는다
  - 여기서 `x` 는 원본의 인덱스
  - `a`는 `ad`에 있는 숫자인데, 숫자 하나씩 넣어야 해서, `for문`도 같이 사용한다
  - 만약에 `ad` 있는 숫자 그대로 넣으면 원본에 역순으로 저장이 된다.
    - 즉 `ad`를 역순으로 순회해야 한다





### 3456 직사각형 길이찾기

> 직사각형 변 3개가 주어지고 나머지 한 변을 찾는 문제다.
>
> 정사각형은 변 4개가 다 동일함으로, if문을 통해 변을 바로 구했다.
>
> 직사각형 같은 경우 변이 2개씩 동일하다.
>
> 그래서 elif문을 써서 나머지 변의 길이를 구했다.

```python
T = int(input())

for t in range(1, T + 1):
    # 세 변의 수는 항상 주어지기 때문에 입력 값으로 넣는다
    a, b, c = map(int, input().split())
    # 세 변의 수가 같으면 무조건 정사각형이다

    # 따라서 나머지 변의 길이도 같다
    if a == b == c:
        print(f'#{t} {a}')
    # a 와 b가 같으면 나머지 변의 길이는 c
    elif a == b:
        print(f'#{t} {c}')
    # a와 c가 같으면 나aj지 변의 길이는 b
    elif a == c:
        print(f'#{t} {b}')
    # b와 c가 같으면 나머지 변의 길이는 a
    elif b == c:
        print(f'#{t} {a}')
--------------------------------------------------------------------
T = int(input())

for t in range(1, T + 1):
    
    side = list(map(int, input().split()))

    dic = {}
	# 딕셔너리에 변의 길이들을 key로 저장한다
    # 변의 길이가 2개 이상이면, value에 1을 누적시킨다
    for i in side:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
	
    # 변의 길이의 value가 2가 아니면 변의 길이를 출력한다
    # 사각형에서 3 변의 길이가 같으면 정사각형
    	# 모든 변의 길이는 같다
    # 사각형에서 2 변의 길이가 같으면 직사각형
    	# 남은 한 변의 길이는 구해야할 변의 길이와 같다
    for key, value in dic.items():
        if value != 2:
            print(f'{t} {key}')
```

- 딕셔너리를 이용해서, 리스트에 있던 값들을 key로 그리고 개수를 value로 넣는다
  - 딕셔너리 value를 가지고 문제를 해결한다



### 10505 소득 불균형

> 사람 인원이 주어지고, 각자의 소득이 주어졌다.
>
> 소득을 다 더한 후, 사람 인원을 나누어 평균 소득을 구했다.
>
> 그리고 소득들을 순회하며 평균 소득보다 같거나 낮으면 리스트에 다시 넣었다.
>
> 그리고 리스트의 길이를 구함으로 문제를 풀었다.

```python
T = int(input())

for t in range(1, T + 1):
    # 사람 인원
    num_ppl = int(input())
    # 소득을 정수 형태로 리스트에 넣기
    income = input().split()
    income = list(map(int, income))

    # 소득을 다 더하고, 인원으로 나누면 평균이 구해짐
    avg = sum(income) / num_ppl

    # 평균 소득보다 낮거나 같으면 리스트 안에 넣기
    low_income = []
    for i in income:
        if i <= avg:
            low_income.append(i)
    
    print(f'#{t} {len(low_income)}')
```



### 10804 문자열의 거울상

> 먼저 문자열을 `[::-1]` 을 통해 뒤집었다
>
> 그 이후 `for문`, `if문`, `elif문`을 통해서 b와 d를 바꾸고 q와 p를 바꿨다.
>
> 바꿀 떄 `.replace()` 메서드를 사용했다

```python
T = int(input())

for t in range(1, T + 1):
    # 문자열 입력
    s = input()
    # 문자열을 인덱스를 이용하여 반대로 돌리기
    rev_s = s[::-1]

    letters = []
    # b면 d로 / d면 b로 / p면 q로 / q면 p로 변환해야한다
    # 단어 하나씩 순회하면서, 바꾸고, 리스트에 넣어준다
    for letter in rev_s:
        if letter == 'q':
            letter = letter.replace('q', 'p')
            letters.append(letter)
        elif letter == 'p':
            letter = letter.replace('p', 'q')
            letters.append(letter)
        elif letter == 'd':
            letter = letter.replace('d', 'b')
            letters.append(letter)
        elif letter == 'b':
            letter = letter.replace('b', 'd')
            letters.append(letter)
    
    # .join을 통해서 str으로 반환
    result = ''.join(letters)

    print(f'#{t} {result}')
----------------------------------------------------------------------------
# 리뷰에서 딕셔너리를 활용해보라고 함

T = int(input())

for t in range(1, T + 1):
    # 문자열 입력
    s = input()
    # 문자열을 인덱스를 이용하여 반대로 돌리기
    rev_s = s[::-1]
    
	# 딕셔너리에 key를 원래 문자열의 문자들을 넣고,
    # value에 반대되는 문자들을 넣는다
    dict_ = {'p': 'q', 'q' : 'p', 'd': 'b', 'b': 'd'}

    letters = []
    
	# rev_s를 순회하면서 딕셔너리에 해당 문자가 있으면
    # .get(i)를 해서 해당 key의 value를 가지고 온다
    for i in rev_s:
        if i in dict_:
            letters.append(dict_.get(i))

    result = ''.join(letters)
    print(f'#{t} {result}')
```

- **딕셔너리를 활용해서 더 짧게 만들기**
  - 처음에 했던 것과 비슷하다
  - 단 문자들을 딕셔너리에 저장을 시켜 놓고, 그 반대되는 문자들을 value로 저장했다



### 14649 신용카드 만들기 1

> 원래 index의 홀수는 2를 곱하고, 짝수는 그냥 더했다.
>
> 근데 리스트의 인덱스 자체가 0부터 시작하여, 짝수번째의 값을 2로 곱하고, 홀수번째의 값을 그냥 더했다.
>
> result라는 변수를 만들어 더해진 값을 누적 시켰다.
>
> 그리고 10을 나누어, 나누어 떨어지면 0을 출력했다.
>
> 만약 안 나눠지면, 10을 나누어 떨어진 수에 뺐다.

```python
T = int(input())

for t in range(1, T + 1):
    num = map(int, input().split())
    nums = list(num)

    result = 0
    for i in range(len(nums)):
        if (i) % 2 == 1:
            result += nums[i]
        else:
            result += (nums[i] * 2)
    

    if result % 10 == 0:
        print(f'#{t} 0')
    else:
        print(f'#{t} {10 - result % 10}')
```



### 14654 신용카드 만들기 2

> 일다 먼저 `.replace()` 통해 '-'를 없앴다.
>
> 그리고 if문을 통해 3, 4, 5, 6, 9로 리스트가 시작하면 `lst` 라는 새로운 리스트에 넣었고, 그게 아니면 바로 0으로 출력했다.
>
> for문을 통해 해당 lst 안에 들어가 있는 숫자들의 길이가 16개면 1을 출력하고, 아니면 0을 출력했다.

```python
T = int(input())

lst = []
for i in range(1, T + 1):
    nums = (str(input()))
    nums = list(nums.replace('-',''))

    lst = []
    if nums[0] == '3' or nums[0] == '4' or nums[0] == '5' or nums[0] == '6' or nums[0] == '9':
    # if nums[0] in '34569':
    # in 을 써서 더 간결하게 만들 수 있다
        lst.append(nums)
    else:
        print(f'#{i} 0')


    for valid in lst:
        if len(valid) == 16:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
```





