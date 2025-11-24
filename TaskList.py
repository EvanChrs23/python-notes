class Task:

    def __init__(self, task):
        self.task = task
        self.status = False

    def mark_as_done(self):
        self.status = True

tasks = Task("washing the dishes")
print(tasks.task, tasks.status)
tasks.mark_as_done()
print(tasks.task, tasks.status)