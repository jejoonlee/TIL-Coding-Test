# 📋DataBase 모델링

### Practice

[syllaverse](#syllaverse)

[학사](#학사)



### Category

[모델링](#%EF%B8%8F-모델링)

​		[ERD](#erd)

​		[정규화](#정규화)



## ✔️ 모델링

> 데이터베이스의 구조나 형식으로 모델 구조만 보고 어떤 데이터를 다루는지 알 수 있음

- **개념적 데이터 모델링**
  - 데이터의 요구사항을 찾고 분석하는 과정, 핵심 개체(Entity) 사이의 관계를 찾아내고 표현
- **논리적 데이터 모델링**
  - 데이터베이스 설계 프로세스의 과정으로 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법/과정
- **물리적 데이터 모델링**
  - 논리적 데이터 모델이 데이터 저장소로서 어떻게 실제로 저장될 것인가



### ERD

> Entity Relation Diagram - 개체 관계 모델

**주요 용어**

- **엔터티 (entity)** : 업무가 관여하는 정보
- **속성 (attribute)** : 엔터티가 가지는 성격, 데이터 타입과 크기 및 제약사항 지정
- **관계 (relationship)** : Entity 간의 관계, 연관성



**관계**

- **카디널리티 (Cardinality) : 수적 관계**
  - **1 : 1 관계** : A는 B를 하나 가진다. B는 A를 하나 가진다
  - **1 : N 관계** : A는 B를 여러 개 가진다. B는 A의 하나에 해당한다
  - **M : N 관계** : A는 B를 여러 개 가진다. B는 A를 여러 개 가진다
- **옵셔널리티**
  - (1) 필수
  - (0) 선택



### Crow's Feet

![Crow-Notation-Chart](DataBase_Basic.assets/Crow-Notation-Chart.png)



![Modelling](DataBase_Basic.assets/Modelling.png)

> 각 값은 하나씩있어야 한다. 두개가 생기게 된다면 새로운 테이블을 만들어서 정규화를 시킨다



### 정규화

> 데이터베이스 테이블을 설계하는 과정에서 중복성을 제거하여 성능을 향상
>
> 테이블을 쪼개는 과정

정규화 종류

- 제 1 정규화 : 도메인 원자값
  - 한 속성에 여러 개의 속성이 포함, 같은 유형의 속성이 여러 개로 나눠져 있는 경우 제거
- 제 2 정규화 : 부분적 함수 종속성 제거
  - PK가 아닌 모든 칼럼은 PK에 종속되도록 구성
- 제 3 정규화 : 이행적 함수 종속성 제거 (X → Y, Y → Z)
  - 일반 속성 간의 함수 종속 관계가 존재하지 않아야 함





## Syllaverse

![syllaverse_curriculum_모델링](DataBase_Basic.assets/syllaverse_curriculum_모델링.png)



## 학사

![학사practice](DataBase_Basic.assets/학사practice-16612435585753.png)



## Netflix DataBase Modelling

![image-20220823195951586](DataBase_Basic.assets/image-20220823195951586.png)
