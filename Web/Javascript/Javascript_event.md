# 📋Web JavaScript

#### Category

[Event](#%EF%B8%8F-Event)

## ✔️ Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
>
> 예) 클릭을 하거나, 스크롤을 하는 등

#### 역할

~~ 하면 ~~ 한다

클릭하면, 경고창을 띄운다. or 특정 이벤트가 발생하면, 할 일(함수)를 등록한다



#### addEventListener

> EventTarget.addEventListener()
>
> - 지정한 이벤트가 대상이 전달된 때마다 호출할 함수를 설정
> - 이벤트를 지원하는 모든 객체 (Element, Document, Window 등)을 대상으로 지정

`target.addEventListener(type, listener[, options])`

- `type` : 반응 할 이벤트 유형 (대소문자 구분 문자열)
- `listener` : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체 / EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함 
