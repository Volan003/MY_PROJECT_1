from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    card_info = card_type_number.split(" ", 1)
    if "Счет" in card_type_number:
        return f"{card_info[0]} {get_mask_account(card_info[1])}"
    else:
        return f"{card_info[0]} {get_mask_card_number(card_info[1])}"


from datetime import datetime


def get_date(date_str: str) -> str:
    """Преобразование даты"""

    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
