from masks import get_mask_card_number, get_mask_account

def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""

    card_info = card_type_number.rsplit(" ", 1)
    if "Счет" in card_type_number:
        return f"{card_info[0]} {get_mask_account(card_info[1])}"
    else:
        return f"{card_info[0]} {get_mask_card_number(card_info[1])}"


print(mask_account_card("Visa Platinum 1596837868705199"))

from datetime import datetime


def get_date(date_str: str) -> str:
    """Преобразование даты"""

    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


#print (get_date ("2024-03-11T02:26:18.671407"))