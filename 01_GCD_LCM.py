# 최대공약수 , 최소 공배수 계산
# 유클리드 알고리즘


# 최대공약수
# a , b  , r 이 있으면
# 한칸씩 이동
# 이동후 r =0 성립시 반환

# 최소 공배수

# a , b , r 의 초기값 저장해둔후
# a / gcd , b / gcd , r / gcd * gcd 로 계산

# 문제
# 두 개의 자연수를 입력받아 최대공약수(GCD)와 최소공배수(LCM)를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000 이하의 자연수이며 사이에 한 칸의 공백이 주어진다.


# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소공배수를 출력한다.


# 함수선언

# 입력

# 출력

# 라인 문제로 나온적 있음

aa, bb = map(int, input().split())

A = int(aa)
B = int(bb)

lcm_mini = A * B

while True:
    r = int(aa) % int(bb)
    if r == 0:
        GCD = int(bb)
        break

    elif r != 0:
        aa = bb
        bb = r

LCM = lcm_mini / GCD

print(int(GCD))
print(int(LCM))
