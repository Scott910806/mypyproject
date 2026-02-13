from concurrent.futures import ThreadPoolExecutor, Future
import threading
import time, random

task_counter = 0
lock = threading.Lock()

def io_task(task_name:str, wait_time:float):
    global task_counter
    print(f"【{time.strftime('%H:%M:%S')}】{task_name} 开始 IO")
    time.sleep(wait_time)
    with lock:
        task_counter += 1
    result = f"{task_name} 结束 IO,已完成任务数{task_counter}"
    print(f"【{time.strftime('%H:%M:%S')}】{result}")
    return result

if __name__ == '__main__':
    start_time = time.time()
    '''
    future_list = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            f:Future = executor.submit(io_task, f"任务{i}", random.random())
            future_list.append(f) # 先搜集Future对象,result()方法会阻塞，等待结果返回
        results = [f.result() for f in future_list]
    for result in results:
        print(result)
    print(f"执行总耗时:{time.time()-start_time}")
    '''

    # 使用executor.map()方法
    with ThreadPoolExecutor(max_workers=5) as executor:
        args_list = [(f"任务{i}", random.random()) for i in range(10)]
        results = executor.map(lambda p : io_task(*p), args_list)
    for result in results:
        print(result)
    print(f"执行总耗时:{time.time()-start_time}")