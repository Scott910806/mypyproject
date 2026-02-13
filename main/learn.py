class A:
    def __init__(self):
        print("A.__init__")
    
    def method(self):
        print("A.method")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()
    
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()
    
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()
    
    def method(self):
        print("D.method")
        super().method()

# 测试初始化顺序
print("=== 初始化顺序 ===")
d = D()

print("\n=== 方法调用顺序 ===")
d.method()