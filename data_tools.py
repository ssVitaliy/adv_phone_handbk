

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


if __name__ == "__main__":
    print_title('kjlkjkllkjlkb', style=1)
    print_title('kjlkjkllkjlkb', style=2)