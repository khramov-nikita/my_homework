from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(input("Введите номер карты: ")))
print(get_mask_account(input("Введите номер счёта: ")))
