def add_prefix_suffix(prefix='', suffix=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{prefix}{result}{suffix}")
            return result

        return wrapper

    return decorator


@add_prefix_suffix(prefix='[', suffix=']')
def greet(name):
    return f"Hello, {name}!"


greet("John")
