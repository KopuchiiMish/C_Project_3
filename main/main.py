from utils.utils import load_operations, get_operation_by_state, sort_by_date, convert_date, hide_card_number, \
    hide_account_number

operations_filename = 'operations.json'

load_operations = load_operations(operations_filename)

s = "EXECUTED"

executed_list = get_operation_by_state(s, load_operations)

sorted_list = sort_by_date(executed_list)

five_latest_operations = sorted_list[:5]

for transaction in five_latest_operations:
    date = transaction.get("date")
    description = transaction.get("description")
    from_ = transaction.get("from")
    to_ = transaction.get("to")
    amount = transaction.get("operationAmount").get("amount")
    currency = transaction.get("operationAmount").get("currency").get("name")

    date = convert_date(date)
    if not from_:
        name_from_ = ""
        hidden_from_number = "отправитель не указан"
    elif "Счет" in from_:
        name_from_ = "Счет"
        hidden_from_number = hide_account_number(from_[-20:])
    else:
        name_from_ = from_[:-17]
        hidden_from_number = hide_card_number(from_[-16:])

    to_ = hide_account_number(to_[-20:])

    print(f'''{date} {description}
{name_from_} {hidden_from_number} -> Счет {to_}
{amount} {currency}
''')
