import time

class Timer:
    def __init__(self, function_to_run):
        self.num_runs = 100
        self.func_to_run = function_to_run
    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(
            "Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )
        return self.func_to_run(*args, **kwargs)

@Timer
def fibonacci(N):
    seq = [1]
    a = 1
    b = 2
    while b < N: 
        c = a + b 
        a = b
        b = c
        seq.append(a)
    return seq

if __name__ == "__main__":
    fibonacci(4_000_000)