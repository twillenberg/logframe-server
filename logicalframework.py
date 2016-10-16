from impact import Impact
from outcome import Outcome
import time
import constants

class LogicalFramework(object):
    def __init__(self, project_name, version):
        self.version = version
        self.project_name = project_name
        self.impact = None
        self.outcome = None
        self.outputs = []
        self.assumptions = []
        self.separator = constants.SEPARATOR

    # Version handling.
    def set_version(self, version):
        self.version = version

    def display_version(self):
        print self.project_name, ", Version: %.2f" % self.version
        print time.strftime("%d/%m/%Y"), "@", time.strftime("%I:%M:%S")
        print self.separator



    # Impact handling.
    def set_impact(self, imp):
        self.impact = Impact(imp)

    def add_impact_indicator(self, ind):
        self.impact.add_indicator(ind)

    def display_impact(self):
        self.impact.display()



    # Outcome handling.
    def set_outcome(self, oc):
        self.outcome = Outcome(oc)

    def add_outcome_indicator(self, ind):
        self.outcome.add_indicator(ind)

    def display_outcome(self):
        self.outcome.display()



    # Output handling.
    def add_output(self, op):
        self.outputs.append(op)

    def number_of_outputs(self):
        print "%d Output(s):" % len(self.outputs)
        return len(self.outputs)

    def display_outputs(self):
        for o in self.outputs:
            o.display()



    # Assumption handling.
    def add_assumption(self, assumption):
        self.assumptions.append(assumption)
        print "[logical framework-level assumption added]"

    def display_assumptions(self):
        for a in self.assumptions:
            a.display()
        separate()

    # Displaying the logical framework.
    @staticmethod
    def display_logical_framework():
        print "This is the logical framework:"

    def separate(self):
        print(self.separator)
