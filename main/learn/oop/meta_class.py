# !usr/bin/env python3
# -*- codiing: utf-8 -*-

class DemoMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("\n 元类接收到的 attrs 的内容:")
        for k, v in attrs.items():
            print(f"{k:20} -> {type(v).__name__ :10} ({v})")
        return type.__new__(cls, name, bases, attrs)
    

class DemoClass(metaclass = DemoMetaClass):
    CONST = 100

    def __init__(self):
        self.instance_var = 200 # 实例变量, 不会出现在元类attrs中

    def normal_method(self):
        print("normal method")

    @classmethod
    def class_method(cls):
        print("class method")

    @staticmethod
    def static_method():
        print("static method")

    @property
    def prop(self):
        return "property"
    
if __name__ == '__main__':
    d = DemoClass()
    