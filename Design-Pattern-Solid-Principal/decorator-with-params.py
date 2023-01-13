def decoratorparam(decoparams):
    def decorator(func):
        def wrapper(*args, **kwargs):
          ans = func(*args, **kwargs)
          return ans
        return wrapper
    return decorator

@decoratorparam("deco-with-param")
def main(a, b):
    print("hello", a, b)


main(1, 2)
