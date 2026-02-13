import asyncio, time

async def worker(name, delay):
    print(f"[{time.strftime('%X')}]{name} 开始任务，预计耗时{delay}s")
    await asyncio.sleep(delay)
    print(f"[{time.strftime('%X')}]{name} 完成任务")

async def main():
    # 注册任务，但并不会立刻启动
    task_a = asyncio.create_task(worker('worker-A', 1))
    task_b = asyncio.create_task(worker('worker-B', 2))
    task_c = asyncio.create_task(worker('worker-C', 1.5))

    print(f"[{time.strftime('%X')}] 准备启动任务")
    # 显式让出线程
    await asyncio.gather(task_a, task_b, task_c) 
    print(f"[{time.strftime('%X')}] 所有任务已完成")

if __name__ == '__main__':
    asyncio.run(main())
    