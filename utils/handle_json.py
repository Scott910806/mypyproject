# !usr/bin/env python3
# --*-- coding: utf-8 --*--

import json, random
from jmespath import compile

def get_data_from_json_by_jmespath(json_data, json_path):
    try:
        data = json.loads(json_data)
        try:
            expr = compile(json_path)
            matches = expr.search(data)
            return matches
        except Exception as e:
            # jsonpath解析异常
            return "Invalid json_path: " + str(e)
    except Exception as e:
        # json解析异常
        return "Invalid json_data: " + str(e)

def get_random_ele(list):
    """
    随机返回list中的元素
    """
    try:
        random_ele = random.choice(list)
        return random_ele
    except IndexError:
        return None

if __name__ == '__main__':
    from collections import defaultdict
    word_summary = defaultdict(list)
    word_summary['scott'].append('python')
    word_summary['scott'].append('java')
    print(word_summary)