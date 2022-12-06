
class Task:
    # comments = []
    # completed = False

    def __init__(self, name, due_date):
        self.due_date = due_date
        self.name = name
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return f"Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        result = []
        if len(self.comments) - 1 >= comment_number >= 0:
            self.comments[comment_number] = new_comment
            for comment in self.comments:
                result.append(comment)
            return ', '.join(result)
        else:
            return f"Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

