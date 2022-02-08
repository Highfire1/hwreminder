from re import sub
from homework.assignment import Assignment
import jsonpickle
from pathlib import Path
from collections import defaultdict


class Homework:

    def __init__(self, /, guild_id):
        self.guild_id = str(guild_id)
        self.path = f"homework\data\{self.guild_id}.json"

        try:
            with open(self.path, 'r') as readfile:
                self.assignments = jsonpickle.decode(readfile.read())
        except:
            self.assignments = []

    def add_assignment(self, subject, description, due_date):
        a = Assignment(subject, description, due_date)
        self.assignments.append(a)
        self.save()
        return a

    def delete_assignment(self, assignment):
        self.assignments.remove(assignment)
        self.save()

    def save(self):
        with open(self.path, 'w') as writefile:
            writefile.write(jsonpickle.encode(self.assignments))
    
    def __str__(self):
        
        if self.assignments == []:
            return "There is NO HOMEWORK!!! :tada::tada::tada: "

        text = ""
        
        sorted = defaultdict(list)
        
        for assignment in self.assignments:
            sorted[assignment.subject].append(assignment)


        for key, value in sorted.items(): 
            
            text += f"**{key}**\n"

            for assignment in value:

                text += f"{assignment.due_date}: "    
                text += assignment.assignment
                text += "\n\n"

        return text
