import time

def func_runtime_period(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {}'.format(end-start))
        return res
    return wrapper