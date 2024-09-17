from db_interface import read_db
from data_tools import (
                    print_title,
                    command_prompt,
                    get_user_data,
                    create_record,
                    valid_user_command,
                    save_record,
                    save_all_records,
                    find_records,
                    )


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
            search_menu()
        elif cmd == 4:
            edit_menu()
        elif cmd == 5:
            delete_menu()

        if cmd == 6:
            break

    print_title('До встречи ;)')


def main_menu() -> int:
    """Выводит главное меню справочника.

    Список команд
        1: чтение всех записей
        2: добавление записи
        3: поиск записи
        4: редактирование записи
        5: удаление записи
        6: выход

    Возвращает:
        (int) валидный номер выбранной команды.
    """

    commands = {
        1: 'чтение всех записей',
        2: 'добавление записи',
        3: 'поиск записи',
        4: 'редактирование записи',
        5: 'удаление записи',
        6: 'выход',
    }
    
    print_title('Главное меню справочника', style=3)
    
    return command_prompt(commands)


def show_menu():
    """Раздел меню 'Чтение всех записей'.
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
    input('Для продолжения нажмите Enter...')


def add_menu():
    """Раздел меню 'Добавление записи'

    Принимает валидные данные от пользователя (имя, фамилию, отчество, телефон).
    Отображает отформатированную запись.
    Спрашивает сохранить или нет. Если да - сохраняет.
    """

    print_title('Добавление записи', style=2)

    name = get_user_data('Введите имя: ')
    surname = get_user_data('Введите фамилию: ')
    last_name = get_user_data('Введите отчество: ')
    phone = get_user_data('Введите телефон: ')

    record = create_record(name, surname, last_name, phone)
    print(f'\nЗапись "{record.strip()}" создана.')
    if valid_user_command('Сохранить? [y/n]: ', ('y', 'n')) == 'y':
        save_record(record)
        print('Запись добавлена в справочник.')
    else:
        print('Запись не сохранена.')
    input('Для продолжения нажмите Enter...')


def search_menu():
    """Меню поиска записей по имени или фамилии.

    Запрашивает ввод строки (имя или фамилию) и выполняет поиск.
    Выводит найденные записи или сообщение 'Записи по запросу не найдены'.
    """
    
    print_title('Поиск записей', style=2)
    records = read_db()
    if records:
        search_request = get_user_data('Введите имя или фамилию: ')
        search_result = find_records(records, search_request)
        if search_result:
            print_title('Найдены записи:', style=2)
            for index in search_result:
                print(f'  {index + 1}: {records[index]}', end='') 
        else:
            print(f'Записи по запросу "{search_request}" не найдены')
    else:
        print('Справочник пуст', '\n')
    input('Для продолжения нажмите Enter...')


def edit_menu():
    """Меню редактирования записей.

    Запрашивает ввод строки (имя или фамилию) и выполняет поиск по имени или фамилии.
        Если найдены несколько записей - запрашивает ввести номер и переходит к редактированию.
        Если найдена только одна запись - переходит к редактированию.
        Если записи по запросу не найдены - выводит сообщение 'Записи по запросу не найдены'
    Просит пользователя ввести новую информацию. После подтверждения - сохраняет.
    """

    print_title('Редактирование', style=2)
    records = read_db()
    if not records:
        print('Справочник пуст, нечего редактировать.', '\n')
    else:
        print_title('Поиск нужной записи', style=1)
        search_request = get_user_data('Введите имя или фамилию: ')
        search_result = find_records(records, search_request)

        if not search_result:
            print(f'Записи по запросу "{search_request}" не найдены')
        else:
            rec_index = None
            if len(search_result) == 1:
                rec_index = search_result[0]
            elif len(search_result) > 1:
                print_title('Найдены несколько записей:', style=1)
                for index in search_result:
                    print(f'  {index + 1}: {records[index]}', end='')
                rec_index = valid_user_command('\nВведите номер нужной: ', tuple([str(i + 1) for i in search_result]))
                rec_index = int(rec_index) - 1
            
            # rec_index содержит индекс изменяемой записи
            print_title('Изменяем запись:', style=1)
            print(records[rec_index])
            name = get_user_data('Введите новое имя: ')
            surname = get_user_data('Введите новую фамилию: ')
            last_name = get_user_data('Введите новое отчество: ')
            phone = get_user_data('Введите новый телефон: ')

            new_record = create_record(name, surname, last_name, phone)
            print(f'\nЗапись "{new_record.strip()}" создана.')
            if valid_user_command('Сохранить? [y/n]: ', ('y', 'n')) == 'y':
                records[rec_index] = new_record
                save_all_records(records)
                print('Запись сохранена.')
            else:
                print('Запись не сохранена.')

    input('Для продолжения нажмите Enter...')


def delete_menu():
    """Меню удаления записей.

    Запрашивает ввод строки (имя или фамилию) и выполняет поиск по имени или фамилии.
        Если найдены несколько записей - запрашивает ввести номер и переходит к удалению.
        Если найдена только одна запись - переходит к удалению.
        Если записи по запросу не найдены - выводит сообщение 'Записи по запросу не найдены'
    Спрашивает пользователя подтверждение на удаление. Если ответ да - удаляет.
    """

    print_title('Удаление записи', style=2)
    records = read_db()
    if not records:
        print('Справочник пуст, нечего редактировать.', '\n')
    else:
        print_title('Поиск нужной записи', style=1)
        search_request = get_user_data('Введите имя или фамилию: ')
        search_result = find_records(records, search_request)

        if not search_result:
            print(f'Записи по запросу "{search_request}" не найдены')
        else:
            rec_index = None
            if len(search_result) == 1:
                rec_index = search_result[0]
            elif len(search_result) > 1:
                print_title('Найдены несколько записей:', style=1)
                for index in search_result:
                    print(f'  {index + 1}: {records[index]}', end='')
                rec_index = valid_user_command('\nВведите номер нужной: ', tuple([str(i + 1) for i in search_result]))
                rec_index = int(rec_index) - 1
            
            # rec_index содержит индекс найденой записи
            if valid_user_command(f'\nУдалить запись "{records[rec_index].strip()}"? [y/n]: ', ('y', 'n')) == 'y':
                deleted_record = records.pop(rec_index)
                save_all_records(records)
                print(f'Запись "{deleted_record.strip()}" удалена из справочника.')
            else:
                print('Удаление отменено.')

    input('Для продолжения нажмите Enter...')


if __name__ == "__main__":
    edit_menu()
