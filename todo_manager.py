from task import Task

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            if task.completed:
                status = '✔'
            else:
                status = ' '    
            print(f'{index}. [{status}] {task.title}')
        if not self.tasks:
            print('У вас нет ни одной задачи')

    def complete_task(self, number):
        task = self.tasks[number - 1]
        task.complete()

    def delete_task(self, number):
        self.tasks.pop(number - 1)        