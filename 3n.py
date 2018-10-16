import time

N = int(input('enter N: '))
summ = 0

MAX = int('9' * 3 * N)
MIN = int('1' + '0' * (3*N-1))

print(MAX)
print(MIN)

start = time.time()

for i in range(MIN, MAX):
    a, b, c = i//10**(N*2), (i%10**(N*2))//10**N, (i%10**(N*2))%10**N

    if a!=0 and b!=0 and c!= 0:
        if i%a==0 and i%b==0 and i%c==0:
            summ += 1
            # print(i,'    ',a,b,c, '     ', summ)

print(start - time.time())
print('TOTAL: {}'.format(summ))
