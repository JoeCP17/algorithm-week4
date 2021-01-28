# Q. 피보나치 수열의 100번째 수를 구하시오.


input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


# 1. 만약 메모에 있으면 그값 반환
# 2. 없으면 아까 수식대로 구한다.
# 3. 그리고 그값을 다시 메모에 기록

# 작동원리 fibo(100) = fibo (99) + fibo(98) .... topdown 방식
# 밑에서 올라오는 프로그램 bottom up방식도있다.
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:  # n의 값이 memo에 있다면
        return fibo_memo[n]  # memo안 에있는 n값 반환

        # 계산 값을 aa에 저장하고
    aa = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = aa  # 저장된 값이들은 aa를 memo에 넣어준다.
    return aa


print(fibo_dynamic_programming(input, memo))
