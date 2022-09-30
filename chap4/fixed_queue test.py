# 고정길이 스택 클래스 FixedQueue 사용
from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    #메뉴선택
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='    ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedQueue(64) # 최대 64개를 인큐 할 수 있는 큐

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 데이터를 입력하세요.: '))
        try:
            s.enque(x)
        except FixedQueue.Full:
            print('가득찼습니다.')
    
    elif menu == Menu.디큐:
        try:
            x = s.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('비어있습니다.')
    
    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('비어있습니다.')

    elif menu == Menu.검색:
        x = int(input('검색할 값을 입력하세요: '))
        if x in s:
            print(f'{s.count(x)}개를 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('찾을 수 없습니다.')
    
    elif menu == Menu.덤프:
        s.dump()
    
    else:
        break
