import random
#피보나치 수 구하기
n = random.sample(range(45), 10)
fibo = [0, 1]
def fibonacci(num) :
    for i in range(2, num+1) :
        fibo.append(fibo[-1] + fibo[-2])

fibonacci(max(n))
for i in n :
    print(i, " : ", fibo[i])