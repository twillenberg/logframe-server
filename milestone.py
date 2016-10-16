#!/usr/bin/python


class Milestone(object):
    def __init__(self, num, description, milestone_type, parent):
        self.num = num
        self.description = description
        self.milestone_type = milestone_type
        self.parent_indicator = parent

    def display(self):
        print "Milestone:", self.num, " description:", self.description, " milestone type:", self.milestone_type, " indicator:", self.parent_indicator
