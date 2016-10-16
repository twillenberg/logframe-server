def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)


class _AssumptionLevel(object):
    @constant
    def IMPACT():
        return "Impact"

    @constant
    def OUTCOME():
        return "Outcome"

    @constant
    def OUTPUT():
        return "Output"

SEPARATOR = "__________________________________________________________\n"
