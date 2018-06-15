import time
import test
import timeit

def count(limit):
    result = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break

                if c * c == (a * a + b * b):
                    result += 1
    return result


if __name__ == '__main__':
    start = time.time()
    result = test.count(1000)
    duration = time.time() - start
    print(result, duration)