# def outer_function():
#     message="hi"
#     def inner_function():
#         print(message)
#         pass 
#     return inner_function()

# print(outer_function())

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#         pass
#     return inner_function()

# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#         pass
#     return wrapper_function()

# hi_func=outer_function("hi")
# bye_func=outer_function("Bye")

# print(hi_func)
# print(bye_func)


# def decorator_function(original_func):
#     def wrapper_function():
#         print("wrapper function ran before {} function".format(original_func.__name__))
#         return original_func
#     return wrapper_function()

# #@decorator_function #thsi line and decorated display line are same
# def display():
#     return print("display func ran")
# # print(display())

# decorated_display=decorator_function(display) #this line and @decorator function line are same
# print(decorated_display())

#Another way of using decorator topic using class 

# def decorator_function(original_func):
#     def wrapper_function(*args,**kwargs):
#         print("wrapper function ran before {} function".format(original_func.__name__))
#         return original_func
#     return wrapper_function(*args,**kwargs)

# class decorator_class(object):
#     def __init__(self,original_func):
#         self.original_func=original_func

#     def __call__(self, *args, **kwargs):
#         print("call method executed this befor {}".format(self.original_func.__name__))
#         return self.original_func(*args,**kwargs)

# @decorator_class
# def display():
#     print("display func executed")
# print(display())

# @decorator_class
# def display_info(name,age):
#     print('my name is {} and my age is {}'.format(name,age))

# print(display_info("anuj",19))

# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename="{}.log".format(orig_func.__name__),level=logging.INFO)

#     def wrapper(*args,**kwargs):
#         logging.info(
#             "Ran with args {} and kwargs {}".format(args,kwargs))
#         return orig_func(*args,**kwargs)

# def my_time(orig_func):
#     import time
    
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         result=orig_func(*args,**kwargs)
#         t2=time.time() - t1
#         print("ran {} in: {}sec".format(orig_func.__name__,t2))
#         return result
#     return wrapper

# import time

# @my_time
# # @my_logger
# def display_info(name,salary):
#     time.sleep(1)
#     print("display_info ran with arguments ({},{})".format(name,salary))

# display_info("anuj",50000)

#Decorator with arguments
def prefix_decorator(prefix):
    def decorator_function(orig_func):
        def wrapper_function(*args,**kwargs):
            print(prefix,"Executed before",orig_func.__name__)
            result=orig_func(*args,**kwargs)
            print(prefix,"Executed after",orig_func.__name__)
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator("Testing:")
def display_info(name,age):
    print("my name is {} and my age is {}".format(name,age))

display_info("anuj",19)