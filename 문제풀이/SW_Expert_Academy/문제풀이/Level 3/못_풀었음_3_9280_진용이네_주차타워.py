import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for t in range(1, T + 1):
  n, m = map(int, input().split())
  
  parking_cost = []
  car_weight = []
  result = 0

  for _ in range(n):
    parking_cost.append(int(input()))

  for _ in range(m):
    car_weight.append(int(input()))

  parking_cost.sort()
  # 주차장에 있는 차의 숫자
  parking = [0] * n
  waiting_line = deque([])
  
  # 세울 곳
  park = 0

  for _ in range(2 * m):
    car = int(input())
    if 0 in parking:
      