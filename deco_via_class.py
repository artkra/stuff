class DecoNoArgs(object):
    def __init__(self, f):
        self._f = f
        self._cached = None

    def __call__(self, *args, **kwargs):
        res = str(self._f(*args, **kwargs))
        self._cached = res
        return 'great ' + res

    def __getattr__(self, key):
        return self._cached


class DecoWithArgs(object):
    def __init__(self, helper):
        self._helper = helper

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            name = f.__name__
            self.name = f(*args, **kwargs)
            return self._helper + ' ' + f(*args, **kwargs)

        return wrapped


# foo = Deco('hello')(foo)
@DecoWithArgs('hello')
def foo():
    return 'world'

@DecoNoArgs
def bar(s):
    return s


if __name__ == '__main__':
    print foo()
    print bar('world')
    print bar.foo
