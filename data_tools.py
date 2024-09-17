from db_interface import db_append, read_db, db_write_all


def print_title(title: str, style: int = 1) -> None:
    """Печатает заголовок title с обрамлением.

    Вариант стиля задаётся аргументом style (по умолчанию = 1):

        style 1
        -------

        style 2
        =======

        style 3
        *******
    """

    style_symbol = ' '

    if style == 1:
        style_symbol = '-'
    elif style == 2:
        style_symbol = '='
    elif style == 3:
        style_symbol = '*'

    print(f'\n{title}\n{style_symbol * len(title)}')


def command_prompt(commands: dict[int, str]) -> int:
    """Выводит список доступных команд.
    
    Принимает (dict) словарь команд в формате [номер команды (int): описание (str)]
    
    Возвращает:
        (int) валидный номер выбранной команды.
    """

    while True:
        answer = input(
            'Возможные действия:\n'
            f'{"\n".join([f"  {var}: {commands[var]}" for var in commands])}'
            '\nВведите номер команды: '
        )
        if answer.isnumeric() and int(answer) in commands:
            return int(answer)
        
        print('\nНеверный ввод\n')


def get_user_data(prompt: str) -> str:
    """Печатает запрос (prompt) и проверяет ввод пользователя.
    
    Если пользователь ввел пустую строку или в ней присутствует символ ';'
    выводит подсказку и повторяет запрос.

    Возвращает валидную строку.
    """

    while True:
        user_input = input(prompt)
        if not user_input:
            print('Строка не может быть пустой')
        elif ';' in user_input:
            print('Строка не может содержать символ ";"')
        else:
            return user_input


def valid_user_command(prompt: str, options: tuple[str]) -> str:
    """Выводит запрос (prompt) и принимает ответ от пользователя.
    Если ответ имеется в кортеже доступных вариантов (options) - возвращает ответ.
    Если нет - выводит подсказку и повторяет запрос.
    
    Возвращает валидный ответ.
    """

    while True:
        answer = input(prompt).lower()
        if answer in options:
            return answer
        else:
            print('Неверный ввод')


def create_record(*args: str) -> str:
    """Возвращает строку, составленную из аргументов (args), разделённых ';'
    и добавляет '\n' в конец строки    
    """

    return ';'.join(args) + '\n'


def save_record(record: str) -> None:
    """Добавляет запись в справочник"""

    db_append(record)
    return


def save_all_records(records: list) -> None:
    """Преобразует список записей в текстовую строку и перезаписывает весь справочник"""
    
    db_write_all(''.join(records))
    return


def find_records(records: list[str], search_request: str) -> list[int]:
    """Ищет в списке (records) записи, поля имя или фамилия которых
    равны строке поиска (search_request). К регистру строк нечувствителен.

    Возвращает список индексов.
    """

    search_request = search_request.lower()
    records = read_db()
    found_records = []
    for index, record in enumerate(records):
        name, surname, *_ = record.split(';')
        if search_request in (name.lower(), surname.lower()):
            found_records.append(index)
    return found_records


if __name__ == "__main__":
    pass