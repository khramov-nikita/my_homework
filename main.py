from src import processing, utils
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Функция, через которую пользователь взаимодействует с программой
    """

    # Объявление некоторых переменных
    is_state: bool
    answer: str
    sort_rub: str
    find_str: str
    to_find: str
    data = []
    data_sorted_by_date = []
    options = {"1": "JSON", "2": "CSV", "3": "XLSX"}
    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    # Начало работы программы
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
        option = input(
            """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n\n"""
        )
        if option in options:
            print(f"Для обработки выбран {options[option]}-файл.")
            break
        else:
            print("Неверный пункт")

    # Программа просит ввести статус операции

    while True:
        status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n"""
        ).upper()
        if status in statuses:
            print(f"Операции отфильтрованы по статусу {status}\n\n")
            break
        else:
            print(f"Статус операции {status} недоступен\n\n")

    # Программа выбирает способ чтения данных
    if option == "1":
        data = utils.reading_json("data/operations.json")
    elif option == "2":
        data = utils.reading_csv("data/transactions.csv")
    elif option == "3":
        data = utils.reading_excel("data/transactions_excel.xlsx")

    data_filtered_by_state = processing.filter_by_state(data, state=status)

    # Программа спрашивает параметры сортировки
    while True:
        answer = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if answer == "да":
            direction = input("\nОтсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n").lower()
            if direction == "по возрастанию":
                is_state = False
            elif direction == "по убыванию":
                is_state = True
            else:
                print("\nНеверный ввод\n")
                continue
            data_sorted_by_date = processing.sort_by_date(data_filtered_by_state, state=is_state)
            break
        elif answer == "нет":
            data_sorted_by_date = data_filtered_by_state
            break
        else:
            print("\nНеверный ввод\n")

    # Программа спрашивает вывести только рублёвые операции
    while True:
        sort_rub = input("\nВыводить только рублевые транзакции? Да/Нет\n").lower()
        if sort_rub == "да":
            data_in_rub = processing.rub_transactions(data_sorted_by_date)
            break
        elif sort_rub == "нет":
            data_in_rub = data_sorted_by_date
            break
        else:
            print("\nНеверный ввод\n")

    # Программа спрашивает слово для поиска по категории
    while True:
        to_find = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if to_find == "да":
            find_str = input("\nВведите слово: ")
            result_list = processing.find_transaction(data_in_rub, find_str)
            break
        elif to_find == "нет":
            result_list = data_in_rub
            break
        else:
            print("\nНеверный ввод\n")

    # Программа выводит результат
    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(result_list)}\n\n")

    if not result_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in result_list:
            print(f'{get_date(transaction["date"])} {transaction["description"]}')
            if "from" in transaction:
                print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
            else:
                print(f'{mask_account_card(transaction["to"])}')
            if "operationAmount" in transaction:
                print(f'Сумма: {transaction["operationAmount"]["amount"]}\n')
            else:
                print(f'Сумма: {transaction["amount"]}\n')


main()
