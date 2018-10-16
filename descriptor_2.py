class Descriptor:
    def __init__(self, val):
        self._val = val

    def __get__(self, obj, type):
        return self._val
    
    def __set__(self, obj, val):
        print('updating ', obj)
        obj.y = 11
        self._val = val

class Foo:
    x = Descriptor(10)
    y = None


if __name__ == '__main__':
    foo = Foo()
    print(foo.x)
    foo.x = 20
    print(foo.x)
    print(foo.y)