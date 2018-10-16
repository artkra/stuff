def deco(s):
    def wrapped(f):
        def res(*args, **kwargs):
            return s + ' ' + f(*args, **kwargs)
        return res
    return wrapped

@deco('hello')
def foo():
    return 'world'


if __name__ == '__main__':
    print foo()
