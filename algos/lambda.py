class Foo(object):
    a = lambda self: self.b()

    def __init__(self):
        self.b =lambda self: None


if __name__ == '__main__':
    foo = Foo()
    print(foo.a())