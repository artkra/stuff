def wrapper(wrapped):
    def res(*args):
        if hasattr(res, '_counter'):
            res._counter += 1
        else:
            setattr(res, '_counter', 1)
        return wrapped(*args)
    return res

@wrapper
def print_some(s):
    return s


if __name__ == '__main__':
    print(print_some('HELLO'))
    print(print_some('HELLO'))
    print(print_some('HELLO'))
    print(print_some('HELLO'))
    print(print_some('HELLO'))
    print(print_some._counter)

