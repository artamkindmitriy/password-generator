import secrets
import string

class PasswordGenerator:
    """Генератор стойких паролей с настраиваемыми параметрами"""
    def __init__(self, length=12, use_digits=True, use_chars=True, use_symbols=True):
        """Инициализирует параметры генератора паролей"""
        self.length = length
        self.use_digits = use_digits
        self.use_chars = use_chars
        self.use_symbols = use_symbols

    @property
    def length(self):
        """Возвращает заданную длину пароля"""
        return self.__length

    @length.setter
    def length(self, value):
        """Проверяет и сохраняет длину пароля"""
        if not isinstance(value, int):
            raise ValueError("Ошибка: длина должна быть числом")

        elif value < 12:
            raise ValueError("Ошибка: минимальная длина пароля - 12")

        self.__length = value

    def generate(self):
        """Формирует и возвращает случайный пароль по выбранным критериям"""
        pool = ""
        password = []

        if self.use_digits:
            pool += string.digits

        if self.use_chars:
            pool += string.ascii_letters

        if self.use_symbols:
            pool += string.punctuation

        if not pool:
            raise ValueError("Ошибка: вы отключили все критерии для создания пароля")

        for i in range(self.length):
            symbol = secrets.choice(pool)
            password.append(symbol)

        return "".join(password)

def run():
    """Запускает интерактивный консольный интерфейс генератора паролей"""
    print("=== Password Generator ===")

    while True:
        try:
            input_length = input("Введите длину пароля (по умолчанию 12): ")

            if input_length == "":
                length = 12
            else:
                length = int(input_length)

            use_digits = input("Добавить цифры? (1 - да, 0 - нет): ") == "1"
            use_chars = input("Добавить буквы? (1 - да, 0 - нет): ") == "1"
            use_symbols = input("Добавить спецсимволы? (1 - да, 0 - нет): ") == "1"

            generator = PasswordGenerator(
                length=length,
                use_digits=use_digits,
                use_chars=use_chars,
                use_symbols=use_symbols
            )

            result = generator.generate()
            print(f"\nРезультат: {result}\n" + "-" * 30)

            choice = input("1. Сгенерировать новый\n 2. Выход\nВыберите пункт: ")

            if choice == "2":
                print("До свидания!")
                break

        except ValueError as exc:
            print(f"\n{exc}\n")
        except Exception as exc:
            print(f"\nПроизошла непредвиденная ошибка: {exc}\n")

if __name__ == "__main__":
    run()
