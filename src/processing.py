def filter_by_state (dictionnary_list, state):
"""Фильтрация словарей по признаку EXECUTED"""

    return [i for i in dictionnary_list if i['state'] == 'EXECUTED']

filter_by_state (dictionnary_list, state = 'EXECUTED')



def sort_by_date(dictionnary_list, ascending=False):
"""Сортировка по дате"""

    sorted_list = sorted(dictionnary_list, key=lambda list_: list_.get('date', 0), reverse=True)
    return sorted_list

#sorted_new_list = sort_by_date(dictionnary_list)
#print(sorted_new_list)
