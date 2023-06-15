import json

def load_operations(operations_filename):

    """Загружает операций студентов из файла"""
    with open(operations_filename) as json_file:
        operation_data = json.load(json_file)
        return operation_data

def get_operation_by_state(state, dict_):
    executed = []
    for item in dict_:
        if item.get("state") == state:
            executed.append(item)
    return executed

def sort_by_date(data):
    data.sort(key=lambda x: x['date'], reverse=True)
    return data

def convert_date(date):
    date = date[:10]
    date = date.split("-")
    new_date = f'{date[2]}.{date[1]}.{date[0]}'
    return new_date

def hide_card_number(c_number):
    new_card_number = f'{c_number[:4]} {c_number[4:6]}** **** {c_number[-4:]}'
    return new_card_number

def hide_account_number(acc_number):
    new_acc_number = f'**{acc_number[-4:]}'
    return new_acc_number

