# 실습 안내

shell_plus 터미널에서 아래 실습 문제들을 해결합니다.
각 실습 문제를 해결하는 코드는 각 문제 코드 블럭에 작성합니다.
실습 완료 후 현재 파일 `실습.md` 을 실라버스에 제출합니다.

# 실습 문제

1. 아래 내용의 데이터 추가하기.
   - content : 실습 제출
   - priority : 5
   - deadline : 2022-09-27

```py
Todo.objects.create(content='실습 제출', priority='5', deadline='2022-09-27')
```

2. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todos = Todo.objects.all().order_by('id')
```

3. 모든 데이터를 deadline을 기준으로 내림차순으로 정렬해서 가져오기.

```py
todos = Todo.objects.all().order_by('-deadline')
```

4. 모든 데이터를 priority가 높은 순으로 정렬해서 가져오기.

```py
todos = Todo.objects.all().order_by('-priority')
```

5. priority가 5인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todos = Todo.objects.filter(priority=5).order_by('id')
```

6. completed가 True인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todos = Todo.objects.filter(completed=True).order_by('id')
```

7. priority가 5인 데이터의 개수

```py
todos = Todo.objects.filter(priority=5)
print(len(todos))
-----------------------------------------------
count = Todo.objects.filter(priority=5).count()
```

8. id가 1인 데이터 1개 가져오기.

```py
todo = Todo.objects.get(id=1)
```

9. id가 1인 데이터 삭제하기.

```py
do = Todo.objects.get(id=1)
do.delete()
```

10. id가 10인 데이터의 priority 값을 5로 변경하기.

```py
do = Todo.objects.get(id=10)
do.priority = 5
do.save()
```