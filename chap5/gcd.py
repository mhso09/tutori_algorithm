# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x:int, y:int) ->int:
    #정수값 x와 y의 최대 공약수를 반환
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == "__main__":
    print("두 수의 최대 공약수를 구합니다.")
    x = int(input('첫째 값 : '))
    y = int(input('둘째 값 : '))
    print(f"두 수의 최대 공약수 {gcd(x,y)}.")
