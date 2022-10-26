def deco(func):
    def wrapper(*ars, **kwargs):
        print("--start")
        func(*args, **kwargs)
        print("--end")
    return wrapper

def y():
    print("test")