from functools import wraps


def decorate_all_functions(function_decorator):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                try:
                    obj = obj.__func__
                except AttributeError:
                    pass
                setattr(cls, name, function_decorator(obj))
        return cls
    return decorator


def print_on_call(func):
    @wraps(func)
    def wrapper(*args, **kw):
        try:
            res = func(*args, **kw)
        except Exception:
            raise Exception('Error in method: '+format(func.__name__), format(func.__doc__))
        return res
    return wrapper


def print_scenario_on_fail(func):
    @wraps(func)
    def wrapper(*args, **kw):
        try:
            res = func(*args, **kw)
        except Exception:
            doc = format(func.__doc__).replace('\n', '')
            doc_arr = doc.split('|')
            for key in doc_arr:
                print(key)
            print('\n')
            raise
        return res
    return wrapper
