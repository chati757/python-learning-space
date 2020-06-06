#see more ..
#https://learning-python.com/rangetest.html

def rangetest(*argchecks):                  # validate positional arg ranges
    def onDecorator(func):
        if not __debug__:                   # True if "python -O main.py args.."
            return func                     # no-op: call original directly
        else:                               # else wrapper while debugging
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator

#1 it's mean check at parameter position 1, position 1 of parameter person function is age.
@rangetest((1, 0, 120))                     # person = rangetest(..)(person)
def person(name, age):
    print('%s is %s years old' % (name, age))

person('test',2) 