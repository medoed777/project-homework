from src.masks import *


if __name__ == "__main__":
    print(get_mask_card_number("1234567891012345"))
    print(get_mask_card_number("1234567891012d"))
    print(get_mask_card_number("123456789101212"))
    print(get_mask_account("1247188571985781"))
    print(get_mask_account("12471as85781"))
    print(get_mask_account("124713262235235285781"))



