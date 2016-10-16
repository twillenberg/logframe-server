#!/usr/bin/python

import debug
import constants

class Output(object):
    def __init__(self, num, name, num_of_indicators):
        self.num = num
        self.name = name
        self.indicators = []
        self.assumptions = []
        self.separator = constants.SEPARATOR

    def id(self):
        return self.id

    def name(self):
        return self.name

    def display(self):
        print self.separator
        return_string = "Output #" + str(self.num) + ": " + self.name + "[" + str(len(self.indicators)) + "]"
        print return_string
        print self.separator

        d = len(self.indicators)
        print "%d Indicator(s):" % d
        for i in self.indicators:
            i.display()

        c = len(self.assumptions)
        print "%d Assumption(s):" % c
        for a in self.assumptions:
            a.display()

    def display_output_number(self):
        return "Output ID#:", self.num

    def display_output_name(self):
        return "Output Name:", self.name

    def display_indicators(self):
        for i in self.indicators:
            i.display()

    def add_indicator(self, ind):
        self.indicators.append(ind)

    def number_of_indicators(self):
        return len(self.indicators)

    def add_assumption(self, assumption):
        self.assumptions.append(assumption)
        if debug.state:
            print "[assumption added]"

