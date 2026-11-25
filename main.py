from todo_manager import TodoManager

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