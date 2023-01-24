def decorator_to_str(function):
    def wrapper(a, b):
        func = function(a, b)
        return str(func)

    return wrapper

@decorator_to_str
def add(a, b):
    return a + b

@decorator_to_str
def get_info(d):
    print(d['info'])
    return d['info']

if __name__ == "__main__":
    print(type(add(1, 1)))
    print(type(get_info({'info': 10})))