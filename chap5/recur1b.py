# 스택으로 재귀 함수 구현 (꼬리 재귀 제거)
from chap4.fixed_stack import Stack # chap4의 stack 함수 사용

def recur(n : int) -> int:
    # 꼬리 재귀를 제거한 recur()함수
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n) # n값 푸시
            n = n - 1
            continue
        if not s.is_empty(): # 스택이 비어있지 않으면
            n = s.pop() # 저장한 값을 n에 pop
            print(n)
            n = n - 2
            continue
        break

x = int(input('수를 입력 : '))

recur(x)
