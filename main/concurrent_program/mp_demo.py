import os, time, random
import multiprocessing as mp

# worker示例
def worker(name:str):
    print("child pid: ", os.getpid())
    start_t = time.time()
    time.sleep(random.random()*3)
    end_t = time.time()
    print(f"{name} costs {end_t - start_t}")

# 使用Queue实现进程之间通信
SENTINEL = None
def worker_plus(task_q:mp.Queue, result_q:mp.Queue):
    for task in iter(task_q.get, SENTINEL):
        task_id, x = task
        time.sleep(0.1)
        result_q.put((task_id, os.getpid(), x, x*x))        
        
if __name__ == "__main__":
    # 一个启动进程的示例
    # p = mp.Process(target=worker, args=("worker-1",))
    # print("before start: pid=", p.pid, "alive=", p.is_alive())
    # p.start()
    # print("after start: pid=", p.pid, "alive=", p.is_alive())
    # p.join()
    # print("after jion: exitcode=", p.exitcode, "alive=", p.is_alive())
    task_q = mp.Queue()
    result_q = mp.Queue()

    # 启动进程
    workers = [mp.Process(target=worker_plus, args=(task_q, result_q)) for _ in range(3)]
    for p in workers:
        p.start()
    
    # 创建任务
    tasks = [1,3,5,7,9,11]
    for task_id, x in enumerate(tasks):
        task_q.put((task_id, x))

    # 插入哨兵，保证worker均能退出 
    for _ in workers:
        task_q.put(SENTINEL)
    
    # 搜集结果
    results = [None]*len(workers) 
    for _ in range(len(workers)):
        task_id, pid, x, y = result_q.get()
        results[task_id] = (pid, x, y) # 通过task_id保持结果顺序
    print(results)