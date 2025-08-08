import json
import jmespath
from datetime import datetime, time

def get_today_min()->str:
    today = datetime.today().date()
    return datetime.combine(today, time.min).strftime("%Y-%m-%d %H:%M:%S")
def get_today_max()->str:
    today = datetime.today().date()
    return datetime.combine(today, time.max).strftime("%Y-%m-%d %H:%M:%S")

def get_current_time()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_json_with_jmespath(json_str, json_path):
    try:
        jmespath_expr = jmespath.compile(json_path)
        return jmespath_expr.search(json.loads(json_str))
    except Exception as e:
        return "Invalid json_path: " + str(e)
    
def find_min_and_max_key(json_str)->list:
    try:
        dict_data = json.loads(json_str)
        keys = list(dict_data.keys())
        sorted_keys = sorted(keys, key=lambda x: int(x))
        return [sorted_keys[0], sorted_keys[-1]]
    except json.JSONDecodeError as e:
        return "Invalid JSON string: " + str(e)

def format_timestamp(timestamp_str:str, format_str="%Y-%m-%d %H:%M:%S")->str:
    if not timestamp_str.isdigit():
        raise ValueError("时间戳必须为数字字符串")
    if len(timestamp_str) not in (10, 13):
        raise ValueError("时间戳长度必须为10或13位")
    if len(timestamp_str) == 13:
        timestamp = int(timestamp_str)/1000
    return datetime.fromtimestamp(timestamp).strftime(format_str)
    

def quick_sort(arr, low, high):
  if low < high:
      # 分区操作，获取分割点
      pi = partition(arr, low, high)
      # 递归排序左子数组
      quick_sort(arr, low, pi)
      # 递归排序右子数组
      quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # 选择中间元素作为基准（可改为随机选择）
    mid = (low + high) // 2
    pivot = arr[mid]
    
    # 双指针初始化
    left = low
    right = high
    
    while True:
        # 左指针寻找大于等于基准的元素
        while arr[left] < pivot:
            left += 1
        # 右指针寻找小于等于基准的元素
        while arr[right] > pivot:
            right -= 1
        # 指针相遇，退出循环
        if left >= right:
            return right
        # 交换左右指针的元素
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    def example():
        x = 10
        y = 20
        print(vars())
        
    example()