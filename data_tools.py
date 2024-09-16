

def print_title(title: str, style: int = 1) -> None:
    """Печатает заголовок title с обрамлением.

    Вариант стиля задаётся аргументом style (по умолчанию = 1):

        style 1
        -------

        =======
        style 2
        =======

        *******
        style 3
        *******
    """

    if style == 1:
        print(f'\n{title}\n{"-" * len(title)}')
    elif style == 2:
        print(f'{"=" * len(title)}\n{title}\n{"=" * len(title)}')
    elif style == 3:
        print(f'{"*" * len(title)}\n{title}\n{"*" * len(title)}')



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
    pass


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


def save_record(data) -> None:
    pass


if __name__ == "__main__":
    valid_user_command('Сохранить? [y/n]: ', ('y', 'n'))