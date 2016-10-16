from constants import _AssumptionLevel


class Assumption(object):
    LEVEL = _AssumptionLevel()

    def __init__(self, level, num, statement):
        self.level = level          # string
        self.num = num              # string
        self.statement = statement  # string

    # Need attributes to determine to what an assumption is linked.

    def display(self):
        print '{0} Assumption %d:'.format(self.level) % self.num, self.statement
