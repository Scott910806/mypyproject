import random
# 冒泡排序
def bubble_sort(arr:list, is_asc=True) -> list:
    n = len(arr)
    if is_asc:
        # 升序
        for i in range(n-1):
            is_swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swapped = True
            if not is_swapped:
                break
    else:
        # 降序
        for i in range(n-1):
            is_swapped = False
            for j in range(n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swapped = True
            if not is_swapped:
                break
    return arr
# 插入排序
def insertion_sort(arr:list, is_asc=True) -> list:
    n = len(arr)
    if is_asc:
        # 升序
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j] > key:
                arr[j+1] = arr[j]
                j-=1  
            arr[j+1] = key
    else:
        # 降序
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j] < key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
    return arr

# 归并排序
'''
1. 取中间位置，将数组分为左右两个子数组
2. 对子数组重复步骤1,继续拆分,知道每个数组只有1个元素(1个元素天然有序)
3. 从下至上依次合并子数组
'''
def merge_sort(arr:list)->list:
    # 递归结束条件
    if len(arr) <=1:
        return arr
    # 拆分
    p = len(arr)//2
    left_arr = merge_sort(arr[:p])
    right_arr = merge_sort(arr[p:])
    return merge(left_arr, right_arr)

# 合并排序结果
def merge(left_arr:list, right_arr:list)->list:
    result = []
    i = j = 0
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result

# 快速排序
'''
1. 在数组中任选一个元素作为比较基准(分割点)
2. 将小于基准的元素放在分割点左边,大于基准点的元素放在分割点的右边
3. 递归调用快速排序算法对分割点左边和右边的子数组进行排序
'''
def quick_sort(arr:list, low:int, high:int)->list:
    # 递归结束条件
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high) 

# 计算分割点 
def partition(arr:list, low:int, high:int)->int:
    # 一般可将开始、末尾元素选作基准元素
    # 为了避免最坏情况，可随机选择基准元素
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    # 将基准元素放到数组末尾
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    # 指针j用于遍历数组找到小于基准值的元素,指针i指向存放小于基准元素区域的末尾
    i = low
    for j in range(low, high):
        if arr[j] >= pivot:
            # 交换操,作节省空间
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    # 将基准元数交换到存放小于基准元素区域的末尾
    arr[i], arr[high] = arr[high], arr[i]
    return i

# 快速查找:
def quick_select(arr:list, low:int, high:int, k:int):
    p = partition(arr, low, high)
    if low < high:
        if p == k-1:
            return arr[p]
        elif p < k-1:
            return quick_select(arr, p+1, high, k)
        else:
            return quick_select(arr, low, p-1, k)

# 一组N个数，查找其中的第k个最大者:降序排列数组,并返回第k-1个元数
def find_kth_largest(arr:list, k:int) -> int:
    if k > len(arr) or k <=0:
        raise ValueError('k is out of range')
    arr_sorted = bubble_sort(arr, False)
    return arr_sorted[k-1]
# 利用快速排序思路查找第k个最大者
def find_kth_largest_plus(arr:list, k:int) -> int:
    if k > len(arr) or k <=0:
        raise ValueError('k is out of range')
    quick_select(arr, 0, len(arr)-1, k)

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 12, 22, 11, 90]
    print(partition(arr, 0, len(arr)-1))
    # print(quick_select(arr, 0, len(arr)-1, 3))
    # print(find_kth_largest(arr, 6))
    