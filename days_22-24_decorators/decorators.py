from functools import wraps


def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return f"<{element}>{func()}</{element}>"

        return wrapper

    return decorator


@make_html("p")
@make_html("strong")
def get_text(text="I code with PyBites"):
    return text


print(get_text())
