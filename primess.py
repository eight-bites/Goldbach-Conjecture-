
N = 100 #граница промежутка от 0 до N, из которого выводим числа

def filling_a(N):
    a = []
    for i in range(1,N+1):
        a.append(i)
    return a


def sorting_a(sieve):
    n=len(sieve)
    for i in range(1,n):
        current = sieve[i]
        if current == -1:
            continue
        pos = i + current
        while pos < n:
            sieve[pos] = -1
            pos += current
    return sieve

def pad(N,W):
    if N < 10:
        return '   '+str(N)
    if N< 100:
        return '  ' + str(N)
    return ' '+str(N)

def printing_table(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(pad(A[i]+A[j], 2),end='')
        print()


def main(n):
    b = []
    Primes = sorting_a(filling_a(n))
    for i in range(n):
        if Primes[i] > 0:
           b.append(Primes[i])
    printing_table(b)




main(N)

