from managers.notes import *
from managers.tasks import *
from managers.contacts import *
from managers.finance import *
from managers.calculator import *


def notes_menu():
    manager = NoteManager()
    while True:
        print("\n--- Меню заметок ---")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Вернуться в главное меню")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            title = input("Введите заголовок: ")
            content = input("Введите содержание: ")
            print(manager.create_note(title, content))
        elif choice == "2":
            for note in manager.see_list_notes():
                print(f"ID: {note.id}, Title: {note.title}, Content: {note.content}, Timestamp: {note.timestamp}")
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            title = input("Новый заголовок (или Enter для пропуска): ")
            content = input("Новое содержание (или Enter для пропуска): ")
            print(manager.update_note(note_id, title, content))
        elif choice == "4":
            note_id = int(input("Введите ID заметки: "))
            print(manager.delete_note(note_id))
        elif choice == "5":
            main()
        else:
            print("Неверный ввод. Попробуйте снова.")


def tasks_menu():
    manager = TaskManager()
    while True:
        print("\n--- Меню задач ---")
        print("1. Создать задачу")
        print("2. Просмотреть все задачи")
        print("3. Обновить задачу")
        print("4. Удалить задачу")
        print("5. Экспорт задач")
        print("6. Импорт задач")
        print("7. Вернуться в главное меню")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            title = input("Введите заголовок: ")
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет задачи (Высокий, Средний, Низкий): ")
            due_date = input("Введите дедлайн задачи в формате ДД-ММ-ГГГГ: ")
            print(manager.create_task(title, description, done=False, priority=priority, due_date=due_date))
        elif choice == "2":
            for task in manager.see_list_tasks():
                print(
                    f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Priority: {task.priority}, Due Date: {task.due_date}")
        elif choice == "3":
            task_id = int(input("Введите ID задачи: "))
            title = input("Новый заголовок (или Enter для пропуска): ")
            description = input("Новое описание (или Enter для пропуска): ")
            priority = input("Новый приоритет (или Enter для пропуска): ")
            due_date = input("Новый дедлайн (или Enter для пропуска): ")
            print(manager.update_task(task_id, title, description, priority, due_date))
        elif choice == "4":
            note_id = int(input("Введите ID задачи: "))
            print(manager.delete_task(note_id))
        elif choice == "5":
            file_path = input("Введите путь для экспорта (например, tasks.csv): ")
            print(manager.export_to_csv(file_path))
        elif choice == "6":
            file_path = input("Введите путь для импорта (например, tasks.csv): ")
            print(manager.import_from_csv(file_path))
        elif choice == "7":
            main()
        else:
            print("Неверный ввод. Попробуйте снова.")


def contacts_menu():
    manager = ContactManager()
    while True:
        print("\n--- Меню контактов ---")
        print("1. Создать контакт")
        print("2. Просмотреть все контакты")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Экспорт контактов")
        print("6. Импорт контактов")
        print("7. Вернуться в главное меню")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите email: ")
            print(manager.create_contact(name, phone, email))
        elif choice == "2":
            for contact in manager.list_contacts():
                print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, E-mail: {contact.email}")
        elif choice == "3":
            contact_id = int(input("Введите ID контакта: "))
            name = input("Новое имя (или Enter для пропуска): ")
            phone = input("Новый номер телефона (или Enter для пропуска): ")
            email = input("Новый email (или Enter для пропуска): ")
            print(manager.update_contact(contact_id, name, phone, email))
        elif choice == "4":
            note_id = int(input("Введите ID контакта: "))
            print(manager.delete_contact(note_id))
        elif choice == "5":
            file_path = input("Введите путь для экспорта (например, contacts.csv): ")
            print(manager.export_to_csv(file_path))
        elif choice == "6":
            file_path = input("Введите путь для импорта (например, contacts.csv): ")
            print(manager.import_from_csv(file_path))
        elif choice == "7":
            main()
        else:
            print("Неверный ввод. Попробуйте снова.")


def finance_menu():
    manager = FinanceManager()
    while True:
        print("\n--- Меню финансовых операций ---")
        print("1. Создать операцию")
        print("2. Просмотреть все операции")
        print("3. Удалить операцию")
        print("4. Вернуться в главное меню")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            category = input("Введите категорию операции: ")
            amount = input("Введите размер операции: ")
            date = input("Введите дату операции: ")
            description = input("Введите описание операции: ")
            print(manager.create_record(category, amount, date, description=None))
        elif choice == "2":
            for contact in manager.list_records():
                print(f"Category: {contact.category}, Amount: {contact.amount}, Date: {contact.date}, Description: {contact.description}")
        elif choice == "3":
            note_id = int(input("Введите ID операции: "))
            print(manager.delete_record(note_id))
        elif choice == "4":
            main()
        else:
            print("Неверный ввод. Попробуйте снова.")


def main():
    print('\nДобро пожаловать в Персональный помощник!')
    print('1. Управление заметками')
    print('2. Управление задачами')
    print('3. Управление контактами')
    print('4. Управление финансовыми записями')
    print('5. Калькулятор')
    print('6. Выход')

    choice = input("Выберите действие (1-6): ")

    if choice == "1":
        notes_menu()
    elif choice == "2":
        tasks_menu()
    elif choice == "3":
        contacts_menu()
    elif choice == "4":
        finance_menu()
    elif choice == "5":
        calc = Calculator()
        print(f'Сумма: {calc.add(5, 3)}')
    elif choice == "6":
        print("Выход из программы. До свидания!")
    else:
        print("Неверный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()
