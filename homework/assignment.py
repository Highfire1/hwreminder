class Assignment:
    def __init__(self, name, subject, description, due_date):
        self.name = name
        self.subject = subject
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name