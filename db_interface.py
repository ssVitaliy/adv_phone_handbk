import os

from config import DB_FILE_NAME, DB_ENCODING




def db_init() -> None:
    """Проверяет наличие файла с данными в текущем каталоге.
    Если файл не найден - создает пустой. Выводит сообщение.

    Возвращает: None
    """

    if not os.path.exists(DB_FILE_NAME):
        open(DB_FILE_NAME, 'x', encoding=DB_ENCODING).close()
        print(f'Файл данных не обнаружен. Создан пустой файл "{DB_FILE_NAME}"')
    else:
        print(f'Файл данных "{DB_FILE_NAME}" обнаружен')


def read_db() -> list[str]:
    """Читает весь файл.
    Возвращает список строк
    """

    with open(DB_FILE_NAME, 'r', encoding=DB_ENCODING) as f:
        data = f.readlines()
    return data


def db_append(data: str) -> None:
    """Добавляет данные (data) в конец файла"""

    with open(DB_FILE_NAME, 'a', encoding=DB_ENCODING) as f:
        f.write(data)
    return


def db_write_all(data: str) -> None:
    """Перезаписывает данными (data) весь файл"""

    with open(DB_FILE_NAME, 'w', encoding=DB_ENCODING) as f:
        f.write(data)
    return
