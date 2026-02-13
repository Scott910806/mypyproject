import os
import multiprocessing as mp

def worker(x: int):
    if x==3:
        raise ValueError("bad")
    return(os.getpid(), x, x*x)

def add(a:int , b:int):
    return a + b

# 回调函数
def on_ok(res):
    print("ok:", res)
# 回调函数
def on_error(e):
    print("error: ", repr(e))

if __name__ == "__main__":
    # 创建进程池
    num = os.cpu_count()
    with mp.Pool(num) as pl:

        # # 批量提交 + 一次性拿结果（同步）
        # results = pl.map(worker, range(100))
        # for item in results:
        #     print(item)

        # 批量提交多参数任务（同步）
        # results = pl.starmap(add, [(1,2),(3,4),(5,6),(7,8)])
        # for item in results:
        #     print(item)

        # 异步提交单个任务 + 通过 AsyncResult 获取
        # async_results = [pl.apply_async(worker, (i,)) for i in range(100)]
        # results = [r.get() for r in async_results]
        # print(results)

        # 带回调的情况
        for i in range(100):
            pl.apply_async(worker, (i,), callback=on_ok, error_callback=on_error)
        pl.close()
        pl.join()
