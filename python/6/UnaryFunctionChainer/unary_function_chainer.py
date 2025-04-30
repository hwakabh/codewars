def chained(functions, v):
    def f(x):
        for function in functions:
            x = function(x)
        return x
    return f(x=v)
