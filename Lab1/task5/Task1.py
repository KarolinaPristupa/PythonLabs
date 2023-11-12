def func(a):
    return a*a

def decor(fn):
    def function():
        print("SOME")
        fn()
        print("jf")
    return function

