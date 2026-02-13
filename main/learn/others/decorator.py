# !usr/bin/env python3
# --*-- encoding:utf-8 --*--

import time, functools

# 不带参数的装饰器
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
# 带参数的装饰器
def metric_plus(tips):
    def real_wrapper(fn):
        @functools.wraps(fn)
        def warpper(*args, **kw):
            t1 = time.time()
            result = fn(*args, **kw)
            t2 = time.time()
            print(f'{tips}:{fn.__name__}执行耗时{t2-t1}s')
        return warpper
    return real_wrapper

# 类装饰器
class Metric:
    def __init__(self, fn):
        self.fn = fn
        functools.update_wrapper(self, fn)
    
    def __call__(self, *args, **kwds):
        t1 = time.time()
        result = self.fn(*args, **kwds)
        t2 = time.time()
        print(f'{self.fn.__name__}执行耗时{t2-t1}s')
        return result

# 类装饰器带参数 
class MetricPlus:
    def __init__(self, tips):
        self.tips = tips

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwds):
            t1 = time.time()
            result = fn(*args, **kwds)
            t2 = time.time()
            print(f'{self.tips}:{fn.__name__}执行耗时{t2-t1}s')
            return result
        return wrapper

@Metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@MetricPlus('测试')
def slow(x, y, z):
    time.sleep(0.2345)
    return x*y*z

if __name__ == '__main__':
    for i in range(5):
        fast(1,2)
        slow(1,2,3)
    print(fast.__name__)
    print(slow.__name__)