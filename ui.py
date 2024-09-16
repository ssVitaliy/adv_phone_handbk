from data_tools import print_title, command_prompt
from db_interface import read_db

def ui() -> None:
    """Интерфейс пользователя. Навигация по меню.
    Выводит приветствие и прощается при завершении
    """

    print_title('Телефонный справочник приветствует Вас!')

    while True:
        cmd = main_menu()

        if cmd == 1:
            show_menu()
        elif cmd == 2:
            add_menu()
        elif cmd == 3:
            edit_menu()
        elif cmd == 4:
            delete_menu()

        if cmd == 5:
            break

    print_title('До встречи ;)')


def main_menu() -> int:
    """Выводит главное меню справочника.

    Список команд
        1: чтение всех записей
        2: добавление записи
        3: редактирование записи
        4: удаление записи
        5: выход

    Возвращает:
        (int) валидный номер выбранной команды.
    """

    commands = {
        1: 'чтение всех записей',
        2: 'добавление записи',
        3: 'редактирование записи',
        4: 'удаление записи',
        5: 'выход',
    }
    
    print_title('Главное меню справочника', style=3)
    
    return command_prompt(commands)


def show_menu():
    """Раздел меню "Чтение всех записей".
    Отображает все записи справочник и их количество.
    Если записей нет - печатает 'Справочник пуст'.
    """

    print_title('Чтение всех записей', style=2)
    records = read_db()
    if records:
        for num, record in enumerate(records, start=1):
            print(f'  {num}: {record}', end='')
        print('Количество записей:', len(records), '\n')
    else:
        print('Справочник пуст', '\n')


def add_menu():
    pass

def edit_menu():
    pass

def delete_menu():
    pass

if __name__ == "__main__":
    ui()
