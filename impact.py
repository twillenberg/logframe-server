#!/usr/bin/python

import debug


class Impact(object):
    def __init__(self, statement):
        self.statement = statement
        self.indicators = []
        self.assumptions = []

    def display(self):
        print "Impact Statement:", self.statement
        print "Impact-level Indicators:", len(self.indicators)

    def display_indicators(self):
        # Printing the impact indicators goes here...
        for i in self.indicators:
            print "Impact Indicator: ", i.id, " Name:", i.name

    def display_assumptions(self):
        # Printing the impact assumptions goes here...
        for a in self.assumptions:
            a.display()

    def add_indicator(self, ind):
        self.indicators.append(ind)
        if debug.state:
            print "[impact indicator added]"

    def add_assumption(self, assumption):
        self.assumptions.append(assumption)
        if debug.state:
            print "[assumption added]"

    def number_of_assumptions(self):
        print "The logical framework has %d impact-level assumption(s):" % len(self.assumptions)
        return len(self.assumptions)
