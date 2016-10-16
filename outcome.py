#!/usr/bin/python

import debug


class Outcome(object):
    def __init__(self, statement):
        self.statement = statement
        self.indicators = []
        self.assumptions = []

    def display(self):
        print "Outcome Statement:", self.statement
        print "Outcome-level Indicators:", len(self.indicators)

    def display_indicators(self):
        # Printing the outcome indicators goes here...
        for i in self.indicators:
            print "Outcome Indicator: ", i.id, " Name:", i.name

    def display_assumptions(self):
        # Printing the outcome assumptions goes here...
        for a in self.assumptions:
            a.display()

    def add_indicator(self, ind):
        self.indicators.append(ind)
        if debug.state:
            print "[outcome indicator added]"

    def add_assumption(self, assumption):
        self.assumptions.append(assumption)
        if debug.state:
            print "[assumption added]"

    def number_of_assumptions(self):
        print "The logical framework has %d outcome-level assumption(s):" % len(self.assumptions)
        return len(self.assumptions)
