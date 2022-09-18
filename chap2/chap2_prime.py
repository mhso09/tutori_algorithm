# #1000 이하의 소수를 나열
# counter = 0 # 나눗셈 횟수를 카운트

# for n in range(2, 1001):
#     for i in range(2,n):
#         counter += 1
#         if n % i == 0: #나누어 떨어지면 소수가 아니기에 반복 중단
#             break
#     else: # 나누어 떨어지지 않으면 다음 수행
#         print(n)
# print(f"나눗셈을 실행한 횟수 : {counter}")

# #1000 이하의 소수를 나열 (알고리즘 개선 1)
counter = 0  # 나눗셈 횟수를 카운트
ptr = 0  # 이미 찾은 소수의 개수
prime = [None] * 500   # 소수를 저장하는 배열

prime[ptr] = 2  # 2는 소수이므로 초기값으로 지정
ptr += 1

# for n in range(3, 1001, 2):  # 홀수만을 대상으로 지정
#     for i in range(1, ptr):  # 이미 찾은 소수로 나눔
#         counter += 1
#         if n % prime[i] == 0:  # 나누어 떨어지면 소수가 아니기에 반복 중단
#             break
#     else:
#         prime[ptr] = n  # 소수로 배열에 등록
#         ptr += 1

# for i in range(ptr):  # ptr의 소수를 출력
#     print(prime[i])
# print(f'나눗셈 실행한 횟수 : {counter}')

# #1000 이하의 소수를 나열 (알고리즘 개선 2)
prime[ptr] = 3
ptr += 1

for n in range(5,1001,2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0: # 나누어 떨어지므로 소수가 아니기에 반복 중단
            break
        i += 1
    else:   # 나누어 떨어지지 않으면
        prime[ptr] = n  # 소수로 배열에 등록
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])

print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}')