#!/usr/bin/env  python3

if __name__ == "__main__":
    def fun1(a):
        x = a * 3


        def fun2(b):
            nonlocal x
            return b + x
        return fun2

    test_fun = fun1(4)
    print(test_fun(7))
