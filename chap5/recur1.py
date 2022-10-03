# 순수한 재귀 함수 구현

def recur(n:int) ->int:
    # 순수 재귀 함수 recur 구현 
    if n > 0 :
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('수를 입력 : '))

recur(x)


def recur(n: int) -> int:
    # 순수 재귀 함수 recur 구현 (거꾸로 출력)
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)
