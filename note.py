class Note(object):
    def __init__(self, parent_num):
        self.belongsTo = parent_num

    def print_note(self):
        print('Note ID:', self.belongsTo)
