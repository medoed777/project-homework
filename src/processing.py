def filter_by_state(dictionary_list, state='EXECUTED') -> list:
    """Функция, принимает словарь и фильтрует по значению ключа 'state'"""
    new_dictionary = []
    for dict_item in dictionary_list:
        if dict_item.get('state') == state:
            new_dictionary.append(dict_item)
    return new_dictionary




def sort_by_date(dict_list, date=min) -> list:
    pass