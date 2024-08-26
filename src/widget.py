from src.masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует счета и номера карт"""
    if len(number.split()[-1]) == 16:
        new_number = card_number(number.split()[-1])
        result = f"{number[:16]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_data(old_date: str) -> str:
    """Функция преобразования даты"""
    return f"{old_date[8:10]}.{old_date[5:7]}.{old_date[0:4]}"




