class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True     


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

manager = TodoManager()
while True:
    print('\nTodo Manager')
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Завершить задачу')
    print('4. Удалить задачу')
    print('5. Выйти\n')
   
    choice = input('Выберите действие: ')
    if choice == '1':
        manager.show_tasks()

    elif choice == '2':
        title = input('Введите задачу: ')
        manager.add_task(title)

    elif choice == '3':
        try:
            number = int(input('Введите номер задачи: '))
            manager.complete_task(number)
        except ValueError:
            print('Необходимо ввести число!')
        except IndexError:
            print('Задачи с таким номером нет!')

    elif choice == '4':
        try:
            number = int(input('Введите номер задачи: '))
            manager.delete_task(number)
        except ValueError:
            print('Необходимо ввести число!')   
        except IndexError:
            print('Задачи с таким номером нет!')
            

    elif choice == '5':
        break