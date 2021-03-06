# 분자 분모가 모두 자연수인 두 분수의 합 또한 분자 분모가 자연수인 분수로 표현할 수 있다.
#
# 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오.
#
# 기약분수란 더 이상 약분되지 않는 분수를 의미한다.
#
# 입력
# 첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다.
# 입력되는 네 자연수는 모두 30,000 이하이다.
#
# 출력
# 첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 공백으로 구분하여 순서대로 출력한다.

# 입력
#  2 7
#  3 5

# 출력
# 31 35

def GCD_gasan(bun1, bun2):
    while True:
        r = bun1 % bun2

        if r == 0:
            GCD = bun2
            break
        elif r != 0:
            bun1 = bun2
            bun2 = r

    return GCD


bza1, bun1 = map(int, input().split())
bza2, bun2 = map(int, input().split())

Bunmo = bun1 * bun2 / GCD_gasan(bun1, bun2)

bunza1 = bza1 * (Bunmo / bun1)
bunza2 = bza2 * (Bunmo / bun2)

bunza = bunza1 + bunza2

c = GCD_gasan(bunza, Bunmo)
print(int(bunza / c), int(Bunmo / c))
