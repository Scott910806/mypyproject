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
    print(f"【{time.strftime('%H:%M:%S')}】{task_name} 结束 IO,已完成任务数{task_counter}")

if __name__ == '__main__':
    # 直接使用Thread原生类创建线程
    tasks = [threading.Thread(target=io_task, args=(f"task-{i}", random.random())) for i in range(5)]

    for task in tasks:
        task.start()
    for task in tasks:
       task.join()