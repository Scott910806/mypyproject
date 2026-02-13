class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node{!r}'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)
    
    def deep_first(self):
        yield self
        for c in self:
            yield from c.deep_first()

if __name__ == '__main__':
    def echo_generator():
        received = yield
        print (f"接收到参数: {received}")

    def sub_generator():
        yield 1
        yield 2
        return "Done"
    
    def main_generator():
        result = yield from sub_generator()
        print (f"子生成器返回结果: {result}")
        
    gen = main_generator()
    print(next(gen))
    print(next(gen))
    next(gen)