# 고정 길이 스택 클래스 구현하기 (collections.deque를 사용)
from typing import Any
from collections import deque

class Stack:
    #고정 길이 스택 클래스 (collections.deque를 사용)

    def __init__(self, maxlen: int = 256) -> None:
        #스택 초기화
        self.capacity = maxlen # 스택 크기
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        # 스택에 쌓여있는 데이터 개수를 반환
        return len(self.__stk)

    def is_empty(self) -> bool:
        # 스택이 비어 있는지 판단
        return not self.__stk

    def is_full(self) -> bool:
        # 스택이 가득 차 있는지 판단
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        # 스택에 value를 푸시 (데이터를 넣음)
        self.__stk.append(value)
    
    def pop(self)-> Any:
        # 스택에서 데이터를 팝 (꼭대기 데이터를 꺼냄)
        return self.__stk.pop()
    
    def peek(self)-> Any:
        # 스택에서 데이터를 피크 (꼭대기 데이터를 봄)
        return self.__stk[-1]
    
    def clear(self) -> None:
        # 스택을 비움 (모든 데이터 삭제)
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        # 스택에서 value를 찾아 인덱스를 반환 (없으면 -1 반환)
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        # 스택에 포함되어 있는 value 개수 반환
        return self.__stk.count(value)
    
    def __contains__(self, value:Any) -> bool:
        # 스택에 value가 있는지 판단
        return self.count(value)

    def dump(self) -> int:
        # 덤프(스택안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)
        print(list(self.__stk))