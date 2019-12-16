from functools import wraps

# def upper(func):
#     def wrapper(*args, **kwargs):
#         to_upper = func(*args, **kwargs)
#         return to_upper.upper()
#     return wrapper

# def split(func):
#     def wrapper(*args, **kwargs):
#         to_split = func(*args, **kwargs)
#         return to_split.split()
#     return wrapper

# def join(func):
#     def wrapper(*args, **kwargs):
#         to_join = func(*args, **kwargs)
#         return ",".join(to_join)
#     return wrapper   

# @split
# @upper
# @join
# def say_hi(message):
#     return message

# print(say_hi("jallll vule"))

def decorator(arg1, arg2):

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f"Arguments passed to decorator {arg1}, {arg2}")
            function(*args, **kwargs)
        return wrapper
        return inner_function




@decorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)

print(print_args(1, 2, 3))











