class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
    def add_student(self, name, grade):
        self.roster[grade] = self.roster.get(grade, []) + [name]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        return {key:sorted(value) for key, value in self.roster.items()}