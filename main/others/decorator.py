# !usr/bin/env python3
# --*-- encoding:utf-8 --*--

import time, functools

def metric(fn):
    """
    装饰器包装函数，用于计算并输出被装饰函数的执行时间
    """
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1 = time.time()
        result = fn(*args, **kw)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__ ,t2-t1))
        # 将原函数调用结果返回
        return result
    return wrapper



@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x*y*z

if __name__ == '__main__':
    print(fast(1, 2))
    slow(1, 2, 3)