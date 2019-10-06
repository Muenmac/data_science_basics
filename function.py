# function.py


def hello():
    print("hello world")

hello()

# working with parameters, non-default values at the beginning, defaults at last
def location(name, loc='Germany'):
    print("this is the actual location", loc, "which is greater than", name)
# location("uk")
# using the default value in the function


location("the rest")

