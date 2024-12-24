import inspect

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': inspect.getmodule(obj)
    }

info = introspection_info(42)
print(info)