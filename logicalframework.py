from impact import Impact
from outcome import Outcome
import time
import constants

class LogicalFramework(object):
    def __init__(self, project_name, version):
        self.project_name = project_name
        self.version = version

        self.impact = None
        self.outcome = None

        self.outputs = []
        self.assumptions = []


    # Get/set version and projecct name.
    @property
    def project_name(self):
        return self.project_name

    @project_name.setter
    def project_name(self, value):
        self.project_name = value

    @property
    def version(self, version):
        return self.version

    @version.setter
    def version(self, value):
        self.version = value

    # Displaying the logical framework.
    @staticmethod
    def display_logical_framework():
        print "This is the logical framework:"

    @staticmethod
    def separate(self):
        print(self.separator)

    # Impact handling.
    def set_impact(self, imp):
        self.impact = Impact(imp)

    # Outcome handling.
    def set_outcome(self, oc):
        self.outcome = Outcome(oc)

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
        print(self.separator)


