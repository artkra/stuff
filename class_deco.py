from functools import wraps


def bitch_decorator(cls):
    @wraps(cls)
    def wrapped(*args, **kwargs):
        cls.__str__ = lambda self: 'THIS'
        return cls(*args, **kwargs)
    return wrapped

@bitch_decorator
class Foo:
    def __init__(self):
        pass


if __name__ == '__main__':
    foo = Foo()
    print(foo)
    print(Foo)
