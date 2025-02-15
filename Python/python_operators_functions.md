# 📋Python Operators

[논리 연산자 (Logical Operator)](#%EF%B8%8F-논리-연산자-logical-operator)

[산술 연산자 (Arithmetic Operator)](#%EF%B8%8F-산술-연산자-arithmetic-operator)

[복합 연산자 (In-place Operator)](#%EF%B8%8F-복합-연산자-in-place-operator)

[비교 연산자 (Comparison Operator)](#%EF%B8%8F-비교-연산자-comparison-operator)

[Escape Sequence](#%EF%B8%8F-escape-sequence)

[Sequence-Operator](#%EF%B8%8F-sequence-operator)

[Functions](#%EF%B8%8F-functions)

[Methods](#%EF%B8%8F-methods)

- [시퀀스](#%EF%B8%8F-시퀀스)

  - [문자열 (String Type)](#문자열-string-type)
    - [문자열 탐색, 검증](#문자열-탐색-검증)
    - [문자열 변경](#문자열-변경)

  - [리스트 (List)](#리스트-list)

- [딕셔너리 (Dictionary)](#딕셔너리-dictionary)

### ✔️ 논리 연산자 (Logical Operator)

| 연산자  |                             내용                             |
| :-----: | :----------------------------------------------------------: |
| A and B |      A와 B 모두 True시, `True` / 그렇지 않으면 `False`       |
| A or B  | A와 B 중 하나만이라도 True면, `True` / A와 B 모두 False시, `False` |
|   Not   |                True를 False로, False를 True로                |





### ✔️ 산술 연산자 (Arithmetic Operator)

| 연산자 |   내용   |
| :----: | :------: |
|  `+`   |   덧셈   |
|  `-`   |   뺄셈   |
|  `*`   |   곱셈   |
|  `%`   |  나머지  |
|  `/`   |  나눗셈  |
|  `//`  |    몫    |
|  `**`  | 거듭제곱 |





### ✔️ 복합 연산자 (In-place Operator)

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a// b  |
|  a%=b   | a = a % b  |
| a **=b  | a = a ** b |



### ✔️ 비교 연산자 (Comparison Operator)

| 연산자 |   내용    |
| :----: | :-------: |
|   <    |   미만    |
|   <=   |   이하    |
|   >    |   초과    |
|   >=   |   이상    |
|   ==   |   같음    |
|   !=   | 같지 않음 |





### ✔️ Escape Sequence

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|   `\n`   |     줄 바꿈     |
|   `\t`   |       탭        |
|   `\r`   |   캐리지리턴    |
|   `\0`   | 널 (null, none) |
|   `\\`   |       `\`       |
|   `\'`   | 단일인용부호(') |
|   `\"`   | 이중인용부호(") |





### ✔️ Sequence Operator

| 연산             | 결과                                                     |
| ---------------- | -------------------------------------------------------- |
| s[i]             | s의 i 번째 항목, 0에서 시작                              |
| s[i:j]           | s의 i 에서 j까지의 슬라이스                              |
| s[i:j:k]         | s 의 i 에서 j까지 스탭 k의 슬라이스                      |
| s + t            | s와 t의 이어 붙이기                                      |
| s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                            |
| x in s           | s 의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
| x not in s       | s 의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
| len(s)           | s 의 길이                                                |
| min(s)           | s 의 가장 작은 항목                                      |
| max(s)           | s 의 가장 큰 항목                                        |



## ✔️ Functions

| 함수                    | 역할                                                         |
| ----------------------- | ------------------------------------------------------------ |
| chr()                   | 유니코드에서 알파벳으로 변환해준다 (97~122 → a~z) / 반대 함수 **ord**() |
| format()                | 형식을 바꾸는 것                                             |
| map(function, iterable) | 순회 가능한 데이터구조 (iterable)의 모든 요소에 함수(function)을 적용하고, 그 결과를 map object로 반환. **정의된 함수가 있어야 한다!!!** |
| ord()                   | 알파벳을 입력하면, 알파벳에서 유니코드로 변환해준다 (a~z → 97~122) / 반대 함수 **chr**() |
|                         |                                                              |



## ✔️ Methods

### 문자열 (String Type)

- #### 문자열 탐색/검증

| 문법          | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| **.find(x)**  | x의 첫 번째 위치를 반환. 없으면, - 1을 반환                  |
| **.index(x)** | x의 첫 번째 위치를 반환. 없으면, 오류 발생                   |
| .isalpha()    | is alphabet (알파벳으로 이루어져있나?) / True or False       |
| .isupper()    | is upper (모두 대문자인가?) / True or False                  |
| .islower()    | is lower (모두 소문자인가?) / True or False                  |
| .istitle()    | is title (제목처럼, 앞의 문자가 대문자인가?) / True or False |
| .isalnum()    | 알파벳과 숫자                                                |
| .isdigit()    | 숫자                                                         |



- #### 문자열 변경

| **문법**                              | **설명**                                       |
| ------------------------------------- | ---------------------------------------------- |
| **.replace(old, new [, count])**      | **바꿀 대상 글자를 새로운 글자로 바꿔서 반환** |
| **.strip([chars])**                   | **공백이나 특정 문자를 제거**                  |
| **.split(sep = None, maxsplit = -1)** | 공백이나 특정 문자를 기준으로 분리             |
| **'seperator'.join([iterable])**      | 구분자로 iterable을 합침                       |
| .capitalize()                         | 가장 첫 번째 글자를 대문자로 변경              |
| .title()                              | '나 공백 이후 대문자로 변경                    |
| .upper()                              | 모두 대문자로 변경                             |
| .lower()                              | 모두 소문자로 변경                             |
| .swapcase                             | 대 ↔ 소문자 서로 변경                          |



### 리스트 (List)

| 문법                      | 설명                                                         |
| ------------------------- | ------------------------------------------------------------ |
| **.append(x)**            | 리스트 마지막 항목에 x 추가                                  |
| **.insert(i,x)**          | 리스트 인덱스 i에 항목 x 삽입                                |
| **.remove(x)**            | 리스트 가장 왼쪽에 있는  항목 (첫번째) x를 제거. 항목이 존재하지 않을 경, ValueError |
| **.pop()**                | 리스트 가장 마지막에 있는 항복 반환 후 제거                  |
| **.pop(i)**               | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| **.clear()**              | 모든 항목을 삭제                                             |
| .extend(m)                | 순회형 m의 모든 항목들의 리스트 끝에 추과 (+=과 같은 기능)   |
| **.index(x, start, end)** | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| **.reverse()**            | 리스트를 거꾸로 정렬                                         |
| **.sort()**               | 리스트를 정렬                                                |
| **.count(x)**             | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |





## ✔️ 컬렉션



### 세트

| 문법           | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| .copy()        | 세트의 얕은 복사본을 반환                                    |
| .add(x)        | 항목 x가 세트에 없다면 추가                                  |
| .pop()         | 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제고. 세트가 비어있을 경우, KeyError |
| .remove(s)     | 항목 x를 세트 s에서 삭제. 항목이 존재하지 않을 경우, KeyError |
| .discard(x)    | 항목 x가 세트 s에 있는 경우, 항목 x를 세트 s에서 삭제        |
| .update(t)     | 세트 t에 있는 모든 항목 중 세트 s에 없는 항목을 추가         |
| .clear()       | 모든 항목을 제거                                             |
| .isdisjoint(t) | 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환 |
| .issubset(t)   | 세트 s가 세트  t의 하위 세트인 경우, True 반환               |
| .issuperset(t) | 세트 s가 세트 t의 상위 세트인 경우, True 반환                |



### 딕셔너리 (Dictionary)

| 문법                 | 설명                                                         |
| -------------------- | ------------------------------------------------------------ |
| .clear()             | 모든 항목 제거                                               |
| .keys()              | 딕셔너리 모든 키를 담은 뷰를 반환                            |
| .values()            | 딕셔너리 모든 값을 담은 뷰를 반환                            |
| .items()             | 딕셔너리 모든 키-값의 쌍을 담은 뷰를 반환                    |
| **.get(k)**          | 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 None을 반환 |
| **.get(k, v)**       | 키 k의 값을 반환하는데, 키 k가 딕셔너리에 없을 경우 v를 반환 |
| **.pop(k)**          | 키 k의 값을 반환하고 키 k인 항목ㅇ르 딕셔너리에서 삭제하는데, 키 k가 딕셔너리에 없을 경우 KeyError를 발생 |
| **.pop(k, v)**       | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리에서 삭제하는데, 키 k가 딕셔너리에 없을 경우 v를 반환 |
| **.update([other])** | 딕셔너리의 값을 매핑하여 업데이트                            |
