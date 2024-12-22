import inspect

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': inspect.getmodule(obj)
    }

info = introspection_info(42)
print(info)