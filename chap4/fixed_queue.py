# 고정 길이 큐 클래스 FixedQueue 구현
from typing import Any

class FixedQueue:

    class Empty(Exception):
        # 비어있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리
        pass

    class Full(Exception):
        # 가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리
        pass

    def __init__(self, capacity : int) -> None:
        # 큐 초기화
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 맨 앞 원소 커서
        self.rear = 0 # 맨 뒤 원소 커서
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐의 본체

    