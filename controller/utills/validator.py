import re


def english(length=20, message=None):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (
                    isinstance(var, str) and
                    len(var) <= length and
                    re.match("^[a-zA-Z\s]{2,}$", var)):
                raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


def persian(length=20, message=None):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (
                    isinstance(var, str) and
                    len(var) <= length and
                    re.match("^[آ-ی\s]{2,}$", var)):
                raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


def email(length=20, message=None):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (
                    isinstance(var, str) and
                    len(var) <= length and
                    re.match("^[\w\.]{2,}@^[\w]{2,}.com$", var)):
                raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


def national_code(message=None):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (
                    isinstance(var, str) and
                    len(var) in (10, 12) and
                    re.match("^\d{3}-?\d{6}-?\d{1}$", var)):
                raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


def number(positive=False,message=None):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (isinstance(var, float) or isinstance(var, int)) :
                raise ValueError(message)
            else:
                if not (positive and var>=0):
                    raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


def pattern(regex="", message=""):
    def inner(func):
        def wrapper(*args):
            var = args[1]
            if not (
                    isinstance(var, str) and
                    re.match(regex, var)):
                raise ValueError(message)
            func(args[0], var)

        return wrapper

    return inner


