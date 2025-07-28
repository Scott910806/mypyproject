# !usr/bin/env python3
# -*- codiing: utf-8 -*-

import os
from collections import deque

def search(lines, pattern, history=5):
    privious_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, privious_lines
        privious_lines.append(line)

def triangles():
    """
    生成杨辉三角形的每一行数字。
    :return: 每一行的数字列表，从第一行开始无限生成
    """
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]


if __name__ == '__main__':
    # n = 0        # 0行
    # for t in triangles():
    #     print(t)
    #     n = n + 1
    #     if n == 10:
    #         break

    # print('%2d--%02d' % (3,5))
    # print('%.2f' % 3.14159)

    current_dir = os.path.dirname(__file__)
    target_file = os.path.join(os.path.dirname(current_dir), 'Demo.py')
    print(target_file)

    with open(target_file) as f:
        for line, previous_lines in search(f, 'json解析异常', 5):
            for pline in previous_lines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)