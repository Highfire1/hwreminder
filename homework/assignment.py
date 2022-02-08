import difflib
import dateparser
import time

class Assignment:
    def __init__(self, subject, assignment, due_date):
        self.assignment = assignment
        
        subjectslist = [
            "Calculus", 
            "French",
            "English",
            "CLC",
            "Biology",
            "Physics"
        ]

        choices = difflib.get_close_matches(subject, subjectslist)
        if choices:
            self.subject = choices[0]
        else:
            self.subject = subject

        try:
            due = dateparser.parse(due_date)
            due = time.mktime(due.timetuple())
            due = int(due)
            self.due_date = f" <t:{due}:f> "
        except:
            self.due_date = f"`{due_date}`"