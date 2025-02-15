# [제로베이스] Java 연산자

*출처 : 제로베이스 백엔드 스쿨*





## 연산자



#### +	:	덧셈

#### -	:	뺄셈	

#### *	:	곱셈

#### /	:	나눗셈

#### %	:	나머지 (나눈 후의 나머지)

#### ++	:	1만큼 더하기

#### --	:	1만큼 빼기





#### 복합 대입 연산자

#### num += 1			:	num = num + 1 와 같다

#### num -= num2	:	num = num - num2 와 같다

#### num *= num2	:	num = num * num2 와 같다

#### num /= num2	:	num = num / num2 와 같다





### 관계

#### A > B	:	A가 B보다 큰 것	

#### A < B	:	A가 B보다 작은 것

#### A >= B	:	A가 B보다 크거나 같은 것

#### A <= B	:	A가 B보다 작거나 같은 

#### A == B	:	A와 B가 같은 것

#### A != B	:	A와 B가 다른 것



### 논리

#### A식 && B식	:	A에 대한 식과 B에 대한 식이 모두 맞을 때에 true를 반환

#### A식 || B식	:	A에 대한 식과 B에 대한 식 둘 중에 하나, 또는 모두 맞을 때 true를 반환

#### A식 ! B식	:	결과가 true이면 false로, false이면 true로 반대값을 반환해준다





### 비트 연산자

#### & (and)

> 모두 1 또는 true이어야 true

|   bit1    |   bit2    |  Result   |
| :-------: | :-------: | :-------: |
| 0 (false) | 0 (false) | 0 (false) |
| 0 (false) | 1 (true)  | 0 (false) |
| 1 (true)  | 0 (false) | 0 (false) |
| 1 (true)  | 1 (true)  | 1 (true)  |



#### | (or)

> 두 비트가 모두 0이어야 0, 즉 false
>
> 그 외에는 모두 결과가 1, true 다

|   bit1    |   bit2    |  Result   |
| :-------: | :-------: | :-------: |
| 0 (false) | 0 (false) | 0 (false) |
| 0 (false) | 1 (true)  | 1 (true)  |
| 1 (true)  | 0 (false) | 1 (true)  |
| 1 (true)  | 1 (true)  | 1 (true)  |



#### ^ (XOR)

> bit1과 bit2 가 달라야 1이, 즉 true다
>
> 즉 둘 다 0이거나, 둘 다 1이면 false, 또는 0을 반환한다

|   bit1    |   bit2    |  Result   |
| :-------: | :-------: | :-------: |
| 0 (false) | 0 (false) | 0 (false) |
| 0 (false) | 1 (true)  | 1 (true)  |
| 1 (true)  | 0 (false) | 1 (true)  |
| 1 (true)  | 1 (true)  | 0 (false) |



#### ~

> 1을 0으로, 0을 1로 바꿔준다
>
> 반전을 시켜준다





### 비트 이동 연산자

#### <<

- 비트를 왼쪽으로 이동시키는 것이다 (즉 값이 2배가 된다)
- 6 << 1
  - 00110 에서 01100 이 된다 (십진수로 표현하면 6에서 12)

#### >>

- 비트를 오른쪽으로 이동시키는 것이다 (2배가 감소된다)
- 18 >> 1
  - 10010 에서 01001 이 된다 (십진수로 표현하면 18에서 9가 된다)

#### >>>

- 오른쪽으로 이동시키고, 빈 공간은 0으로 채운다

