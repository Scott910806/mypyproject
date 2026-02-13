import re

s = "Python3.10, Java17, C++20"
pattern1 = r'([a-zA-Z]+\+*)(\d+\.?\d*)'
result = re.finditer(pattern1, s)
for item in result:
    print(f'{item.group(1)}:{item.group(2)}')