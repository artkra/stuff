class Class():

        @classmethod
        def foo(cls, arg):
                print(arg)

        @staticmethod
        def pri():
                print('CLASS')

class SubClass(Class):

        @classmethod
        def foo(cls):
                print('SUBCLASS')

        @staticmethod
        def bar(cla):
                cla.pri()

        @staticmethod
        def pri():
                print('SUBCLASS')

if __name__=='__main__':
        Class.foo(1)
        Class().foo(2)
        SubClass.foo()
        super(SubClass, SubClass).foo(5)
        SubClass.bar(SubClass)
        SubClass.bar(Class)
