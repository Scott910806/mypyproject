#!/bin/bash
# 这是注释：测试Shell脚本
echo "========== 脚本开始执行 =========="
echo "当前目录：$(pwd)"
echo "当前目录下的.log文件数量：$(find ./ -name "*.log" | wc -l)"
echo "当前系统时间：$(date "+%Y-%m-%d %H:%M:%S")"
echo "========== 脚本执行结束 =========="
