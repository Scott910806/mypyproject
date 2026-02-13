from concurrent.futures import ThreadPoolExecutor, as_completed,Future
import time, random

def io_task(task_name: str, wait_time: float):
    print(f"【{time.strftime('%H:%M:%S')}】{task_name} 开始 IO")
    time.sleep(wait_time)
    
    # 模拟某些任务可能会失败
    if "异常" in task_name:
        raise Exception(f"{task_name} 发生异常！")
    
    result = f"{task_name} 结束 IO"
    print(f"【{time.strftime('%H:%M:%S')}】{result}")
    return result

if __name__ == "__main__":
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_index = {} # 构建future和任务入参的字典
        args_list = [
            ("任务0", random.random()),
            ("任务1", random.random()),
            ("异常任务2", random.random()),  # 这个会抛出异常
            ("任务3", random.random()),
            ("任务4", random.random())
        ]
        for i, args in enumerate(args_list):
            future:Future = executor.submit(io_task, *args)
            future_to_index[future] = i
            
        success_results = []
        failed_results = []
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                result = future.result()
                success_results.append((index,result))
                print(f"成功:{result}")
            except Exception as e:
                failed_results.append((index,str(e)))
                print(f"失败:{index}执行失败,异常信息:{str(e)}")
        print(f"成功结果数:{len(success_results)}")
        print(f"失败结果数:{len(failed_results)}")

    print(f"执行总耗时:{time.time()-start_time}")