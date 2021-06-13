
def outer_function(main_function):
    def inner_function(*args, **kwargs):
        func_name = main_function.__name__
        return main_function(func_name_=func_name,*args, **kwargs)
    return inner_function

@outer_function
def say_hello(name,func_name_=''):
    print("hellow {} {}".format(name, func_name_))

say_hello("dumidu")