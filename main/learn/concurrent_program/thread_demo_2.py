import threading
import time, random

task_counter = 0
lock = threading.Lock()

class IOTask(threading.Thread):
    def __init__(self, task_name:str, wait_time:float):
        super().__init__()
        self.task_name = task_name
        self.wait_time = wait_time

    def log(self, msg:str):
        print(f"【{time.strftime('%H:%M:%S')}】{self.task_name} {msg}")

    def run(self):
        global task_counter
        self.log("开始执行")
        time.sleep(self.wait_time)
        with lock:
            task_counter += 1
        self.log(f"结束执行,已完成任务数{task_counter}")

if __name__ == '__main__':
    tasks = [IOTask(f"task-{i}", random.random()) for i in range(5)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()