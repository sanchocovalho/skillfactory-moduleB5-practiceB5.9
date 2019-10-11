import time

NUM_RUNS = 100

class Timer:
    def __init__(self, function_to_run, num_runs=100):
        self.start = 0
        self.num_runs = num_runs
        self.func_to_run = function_to_run
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args, **kwargs):
        timer = time.time() - self.start
        avg = timer / self.num_runs
        fn = self.func_to_run.__name__
        print(
                "Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )

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
    with Timer(fibonacci, NUM_RUNS):
        for _ in range(NUM_RUNS):
            fibonacci(4_000_000)