#!/usr/bin/python3

if __name__ == "__main__":
    """Calculator operation"""
    import calculator_1 as calc
    from calc import add 
    from calc import sub 
    from calc import mul 
    from calc import div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
