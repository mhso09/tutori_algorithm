from typing import Any, MutableSequence, Sequence

# 뮤터블 시퀸스 원소를 역순으로 정렬
def reverse_array(a:MutableSequence) -> None:
    '''뮤터블 시퀸스 a의 원소를 역순으로 정렬'''
    n = len(a)
    for i in range(n//2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('난소의 수를 입력하세요 : '))
    x = [None] * nx # 원소 수가 nx인 리스트 생성
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요 : '))
    
    reverse_array(x) # x를 역순으로 정렬

    print('배열을 정렬하였습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')