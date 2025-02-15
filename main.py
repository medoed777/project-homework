from src.widget import *


if __name__ == "__main__":
    print(get_mask_card_number("1234567891012345"))
    print(get_mask_card_number("1234567891012d"))
    print(get_mask_card_number("123456789101212"))
    print(get_mask_account("1247188571985781"))
    print(get_mask_account("12471as85781"))
    print(get_mask_account("124713262235235285781"))

    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 1234"))
    print(mask_account_card("Maestro 7000792289606361123"))


    print(get_date("2024-03-11T02:26:18.671407"))





