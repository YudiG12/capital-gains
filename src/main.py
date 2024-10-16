import json, fileinput


def main():
    inputLines = fileinput.input()

    for line in inputLines:
        if line == '\n':
            return
            
        operation_list: List[Dict] = json.loads(line)
        print(calculate_operation(operation_list))


def calculate_operation(operation_list, current_total_quantity: int = 0, current_weighted_average_cost: float = 0, loss: float = 0, index: int = 0 , taxes = ()):
    if index == len(operation_list):
        return list(taxes)

    operation = operation_list[index]['operation']
    unitCost = operation_list[index]['unit-cost']
    quantity = operation_list[index]['quantity']

    if operation == 'buy':
        return buy_operation(operation_list, current_total_quantity, current_weighted_average_cost, quantity, unitCost, loss, index, taxes)
    elif operation == 'sell':
        return sell_operation(operation_list, current_total_quantity, current_weighted_average_cost, quantity, unitCost, loss, index, taxes)


def buy_operation(operation_list, current_total_quantity, current_weighted_average_cost, quantity, unitCost, loss, index, taxes):
    return calculate_operation(
            operation_list,
            current_total_quantity + quantity,
            get_weighted_average_cost(current_total_quantity, current_weighted_average_cost, quantity, unitCost),
            loss,
            index + 1,
            taxes + ({'tax': 0.00},)
            )

def sell_operation(operation_list, current_total_quantity, current_weighted_average_cost, quantity, unitCost, loss, index, taxes):
    new_loss = get_loss(current_weighted_average_cost, unitCost, quantity, loss)
    if is_less_or_equal_than_minimal(unitCost, quantity):
        return calculate_operation(
            operation_list,
            current_total_quantity - quantity,
            current_weighted_average_cost,
            new_loss,
            index + 1,
            taxes + ({'tax': 0.00},)
            )
    else:
        if new_loss < 0:
            return calculate_operation(
                operation_list,
                current_total_quantity - quantity,
                current_weighted_average_cost,
                loss,
                index + 1,
                taxes + ({'tax': get_tax_over_profit(unitCost, current_weighted_average_cost, quantity, loss)},)
                )
        else:
            return calculate_operation(
                operation_list,
                current_total_quantity - quantity,
                current_weighted_average_cost,
                new_loss,
                index + 1,
                taxes + ({'tax': 0.00},)
                )

def get_weighted_average_cost(current_total_quantity, current_weighted_average_cost, quantity, unitCost):
    return round(((current_total_quantity*current_weighted_average_cost) + (quantity*unitCost))/(current_total_quantity + quantity),2)


def get_loss(current_weighted_average_cost, unitCost, quantity, loss):
    return round((current_weighted_average_cost - unitCost)*quantity + loss,2)


def is_less_or_equal_than_minimal(unitCost, quantity):
    return round(unitCost*quantity <= 20000,2)


def get_tax_over_profit(unitCost, current_weighted_average_cost, quantity, loss):
    return round(0.20*((unitCost - current_weighted_average_cost)*quantity - (loss)),2)


if __name__ == "__main__": # pragma: no cover
    main()
