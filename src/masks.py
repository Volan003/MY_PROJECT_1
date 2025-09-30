

def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера карты"""

    card_str = str(card_number)
    output_list =(card_str[:4] + " " + card_str[4:6] + "**" + " " + "****" + " " + card_str[-4:])
    return output_list

#print (get_mask_card_number (1234567891234567))


def get_mask_account(card_account: int) -> str:
    """Маскировка номера счета"""

    card_account_str = str(card_account)
    output_list =("**" + card_account_str[-4:])
    return output_list

#print (get_mask_account (1234567891234567))

