from db_interface import db_init
from ui import ui


if __name__ == "__main__":
    # Проверяем существует ли файл данных, если нет - создаём
    db_init()
    # Вызываем пользовательский интерфейс
    ui()


# Функции чтения и записи в файл в модуле db_interface.py
# Функции работы с данными в модуле data_tools.py
# Функции навигации по меню в модуле ui.py