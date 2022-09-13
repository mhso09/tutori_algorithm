from chap2_array import max_of
import random

print("배열의 최댓값을 구합니다.")
print("주의 : 'end'를 입력하면 종료합니다.")

number = 0
x = []
while True:
    s = input(f'x[{number}]값을 입력하세요. : ')
    if s == 'end':
        break
    x.append(int(s)) # 배열의 맨 끝에 추가
    number += 1
print(f'{number}개를 입력했습니다.')
print(f'최댓값은{max_of(x)}입니다.')

# 배열 원소의 최댓값을 구해서 출력하기
print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요 : '))
lo = int(input('난수의 최솟값을 입력하세요 : '))
hi = int(input('난수의 최댓값을 입력하세요 : '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)
print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

# 각 배열 원소의 최댓값을 구해 출력하기(튜플, 문자열, 리스트)
t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']
print(f'{t} 가운데 최댓값은 {max_of(t)}입니다.')
print(f'{s} 가운데 최댓값은 {max_of(s)}입니다.')
print(f'{a} 가운데 최댓값은 {max_of(a)}입니다.')

# 원소 수를 len()함수로 미리 알아내 0에서 원소 수 -1 까지 반복
# list의 모든 원소를 스캔
x = ['johan', 'george', 'paul', 'ringo']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    print()

# 인덱스와 원소를 짝지어 enumerate()함수로 반복해서 꺼냄
# 리스트 모든 원소를 enumerate()함수로 스캔
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    print()
# 위와 같지만 1부터 카운트 시작
for i, name in enumerate(x,1):
    print(f'x[{i}] = {name}')

# 인덱스값을 사용하지 않고 in을 사용하여 원소를 처음부터 순서대로 꺼냄
# 리스트 모든 원소 스캔 (인덱스 번호 사용 안함)
for i in x:
    print(i)
