# 🧑‍💻알고리즘 모의고사 2🧑‍💻

[민석이의 과제 체크하기](#민석이의-과제-체크하기)

[조교의 성적 매기기](#조교의-성적-매기기)

[암호 생성기](#암호-생성기)

[괄호 짝짓기](#괄호-짝짓기)

[파리 퇴치](#파리-퇴치)



### 민석이의 과제 체크하기

그리고 제출한 사람의 목록을 받았다.

수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

```python
# 테스트 케이스 수
for t in range(1, T + 1):
    # 수강생 수, 과제 제출
    stu, hom = map(int, input().split())
    # 과제 제출한 학생
    fin = list(map(int, input().split()))

    # 과제를 제출하지 않은 사람 번호 넣기
    unfin = []
    # 수강생 번호
    for i in range(1, stu + 1):
        if i not in fin:
            unfin.append(i)
            result = sorted(unfin)
            result = ' '.join(map(str, result))

    print(f'#{t} {result}')
```

#### 🚨🚨🚨 **풀이** 🚨🚨🚨

- **Main: 학생들 리스트와 과제를 푼 리스트를 비교 하는 것**

  - 과제를 다 푼 학생들의 리스트를 만든다

  - 학생은 **학생 수로 각자 번호**가 매겨져 있다

    `for i in range(1, stu + 1):`

    - 학생을 한 명씩 순회하며, 

    `if i not in fin:`

    - 과제를 제출한 리스트에 번호가 없으면,

    `unfin.append(i)`

    - 해당 학생은 과제를 제출 안 한 것

    ` result = sorted(unfin)`

    - 그리고 오름차순으로 출력하기 위해, `sorted`로 정렬



### 조교의 성적 매기기

총점 = 중간고사 (35%) + 기말고사 (45%) + 과제 (20%)

입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,

학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,

K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

```python
T = int(input())

for t in range(1, T + 1):
# 학생수 N , 학점을 알고싶어하는 학생의 번호
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())

    scores = [list(map(int, input().split())) for _ in range(N)]

    # 최종 '점수'들을 final_scores 리스트에 저장하기
    final_scores = []
    for i in range(N):
        final_score = (scores[i][0] * 0.35) + (scores[i][1] * 0.45) + (scores[i][2] * 0.2)
        final_scores.append(round(final_score, 3))

    # 최종 '점수'들을 내림차순으로 rank로 저장하기
    rank = sorted(final_scores, reverse = True)

    for i in range(len(rank)):
        if final_scores[K - 1] == rank[i]:
            g = int(i // (N / 10))
            grade = grades[g]
    
    print(f'#{t} {grade}')
```

#### 🚨🚨🚨 풀이 🚨🚨🚨

- 총점 만들기

  - 총점을 만들기 위해서는 `행`을 기준으로 계산을 하면 된다.

  `final_score = (scores[i][0] * 0.35) + (scores[i][1] * 0.45) + (scores[i][2] * 0.2)`

  - 중간고사 비율 / 기말고사 비율 / 과제 비율

- 구해진 총점들을 리스트에 넣는다

  - `final_scores`라는 리스트 : K번째의 학생의 점수를 알 수 있다
  - `rank` : 총 점수들을 내림차순으로 저장되어 있는 변수
    - K번째의 학생이 몇 등을 했는지 알아야,  학점`grade`을 알 수 있다

- `K`번의 학생의 점수를 알아내고, 점수가 몇 등인지 알아낸다

  - 해당 등수를 (N/10)과 나누어 몫을 구한다
    - 학점을 총 10개이고 같은 비율로 나눠진다
    - 그러면 10개의 그룹이 만들어진다.
  - 그 몫을 학점들이 있는 `grades` 리스트 인덱스로 구면 K번째의 학점을 알 수 있다



### 암호 생성기

다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

\- 8개의 숫자를 입력 받는다.

\- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

\- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다

```python
from collections import deque
# popleft()를 사용하기 위해서

for t in range(10):
    T = int(input())       
    nums = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        num_add = nums[0] - cnt
        if num_add > 0:
            nums.append(num_add)
            cnt += 1
            nums.popleft()
            # 1 사이클이 1부터 5를 빼는 것이니깐
            # cnt가 6이 되면 1로 초기화 시킨다
            if cnt == 6:
                cnt = 1
        elif num_add <= 0:
            nums.append(0)
            nums.popleft()
            break

    result = ' '.join(list(map(str, nums)))

    print(f'#{T} {result}')
```

#### 🚨🚨🚨 풀이 🚨🚨🚨

- **중요 포인트**
  - 계산 후 첫 번째 숫자는, 맨 뒤로 간다
  - 5번 계산이 한 사이클
    - 첫 번째 숫자에 -1, -2, -3, -4, -5 씩 뺀다
  - 이 사이클을 마지막 숫자가 0 또는 0이하가 될 때까지 한다. (0 이하 일시, 0으로 통일)
- `nums.append(num_add)` , `nums.popleft()`
  - 뒤에 계산된 0번째 숫자를 삽입하고 `.append()`
  - 0번째 숫자는 뺀다 `.popleft()`



### 괄호 짝짓기

```python
for t in range(1, 11):
    dis = int(input())
    brak = list(input())

    stack = []

    for i in brak:
        if i in '([{<':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '(':
                print(f'#{t} 0')
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '[':
                print(f'#{t} 0')
                break
            elif stack[-1] == '[':
                stack.pop()
        elif i == '}':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '{':
                print(f'#{t} 0')
                break
            elif stack[-1] == '{':
                stack.pop()
        elif i == '>':
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            elif stack [-1] != '<':
                print(f'#{t} 0')
                break
            elif stack[-1] == '<':
                stack.pop()
    else:     
        if len(stack) != 0:
            print(f'#{t} 0')
        else:
            print(f'#{t} 1')
```

#### 🚨🚨🚨 풀이 🚨🚨🚨

**스택 이용하기!**

- 리스트를 순회하며 `( { [ <` 중 하나가 있으면 `stack`에 넣는다
  - 해당 괄호와 맞는 반대쪽 괄호가 나오면 `.pop()`로 `stack`에서 뺀다
  - 순회를 다 했는데, `stack`에 아무것도 없으면 문자열은 **유효**한 것
- 단! 반대쪽 괄호를 넣으려고 했는데, `stack`에 아무것도 없으면 **무효**
- 또한 반대쪽 괄호인데, `stack` 마지막이 다른 괄호인 경우도 **무효**



### 파리 퇴치

```python
T = int(input())

for t in range(1, T + 1):

    N, M = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    total = [[0] * N for _ in range(N)]
	
    # 이차원 리스트를 순회한다
    for x in range(N):
        for y in range(N):

            add = 0
            
            # 순회하면서, x부터 x + M 만큼
            # 그리고 y부터 y + M 만큼을 순회를 한다
            for i in range(x, x + M):
                for j in range(y, y + M):
					
                    # 단 i와 j는 리스트 안에 있어야 하고
                    # 그 조건까지 맞아 떨어지면, add에 누적시킨다
                    if 0 <= i < N and 0 <= j < N:
                        add += area[i][j]
            # 구한 총 값을 total에 넣는다        
            total[x][y] = add
	
    # 최대값 찾기
    max_num = 0
    for x in range(N):
        for y in range(N):
            if total[x][y] > max_num:
                max_num = total[x][y]

    print(f'#{t} {max_num}')
```

