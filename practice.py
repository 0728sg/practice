def moi_decorator(func):
    def wrapper(*args, **kwargs):
        print("prosto vetka:(")
        result = func(*args, **kwargs)
        print("new vetka")
        return result
    return wrapper
@moi_decorator
def say_hello():
    print("Salam")

if __name__ == "__main__":
    say_hello()