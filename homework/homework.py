from homework.assignment import Assignment
import jsonpickle
from pathlib import Path

class Homework:

    def __init__(self, /, guild_id):
        self.guild_id = str(guild_id)
        self.path = f"homework\data\{self.guild_id}.json"

        try:
            with open(self.path, 'r') as readfile:
                self.assignments = jsonpickle.decode(readfile.read())
        except:
            self.assignments = []

    def add_assignment(self, /, name, subject, description, due_date):
        self.assignments.append(Assignment(name, subject, description, due_date))
        self.save()

    def delete_assignment(self, assignment):
        self.assignments.remove(assignment)
        self.save()

    def save(self):
        with open(self.path, 'w') as writefile:
            writefile.write(jsonpickle.encode(self.assignments))
    
    def __str__(self):
        return str(self.assignments)
