# !usr/bin/env python3
# -*- encoding: utf-8 -*-

from enum import Enum, unique

# 通过构造方法直接创建枚举类
Month = Enum('Month', 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec')

Season = Enum('Season', ('Spring', 'Summer', 'Fall', 'Winter'))

Color = Enum('Color', [('Red', 1), ('Green', 2), ('Blue', 3)])

# 通过继承Enum创建枚举类
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    


if __name__ == '__main__':

    # 遍历枚举值
    for month in Month:
        print(month, month.value)
    
    # 另外一种方式遍历
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    print(Month['Jan'])   
    print(Month.Jan.value == 1)