class MyMeta(type):

    def __new__(cls, cls_name, bases, dct):
        upper_dct = {}

        for key, val in dct.items():
            if not key.startswith('__'):
                upper_dct[key.upper()] = val
            else:
                upper_dct[key] = val

        return super(MyMeta, cls).__new__(cls, cls_name, bases, upper_dct)


class Foo(metaclass=MyMeta):
    bar = 1    


if __name__ == '__main__':
    foo = Foo()
    print(hasattr(Foo, 'bar'))
    print(hasattr(Foo, 'BAR'))
    print(foo.BAR)