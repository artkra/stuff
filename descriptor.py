class A(object):

    def __init__(self, a):
        self.a = a

    def __getattribute__(self, key):
        return str(object.__getattribute__(self, key)) + '_PSHOL VZHOPU!'

if __name__ == '__main__':
    o = A(1)
    print(o.a)
