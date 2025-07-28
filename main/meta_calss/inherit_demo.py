# !usr/bin/env python3
# -*- encoding:utf-8 -*-

class Base:
    class_attr = "基类属性"

    def instance_method(self):
        # 调用类方法
        self.__class__.class_method()

        # 修改类属性
        self.__class__.class_attr = "新值"

    @classmethod
    def class_method(cls):
        print(f"类方法调用，当前类属性值: {cls.class_attr}")

class SubClass(Base):
    class_attr = "子类属性" 


if __name__ == "__main__":
    sub = SubClass()
    print(type(sub))
    sub.instance_method()
    print(SubClass.class_attr)