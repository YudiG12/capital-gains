from src.main import *
from io import StringIO

def test_calculate_operation_empty_list():
    operation_list = []
    current_total_quantity = 0
    current_weighted_average_cost = 0
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == []

def test_buy_operation():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 10}]
    current_total_quantity = 0
    current_weighted_average_cost = 0
    loss = 0
    index = 0
    taxes = ()
    assert buy_operation(operation_list, current_total_quantity, current_weighted_average_cost, 10, 10, loss, index, taxes) == [{'tax': 0.00}]

def test_sell_operation_less_than_minimal():
    operation_list = [{'operation': 'sell', 'unit-cost': 10, 'quantity': 10}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert sell_operation(operation_list, current_total_quantity, current_weighted_average_cost, 10, 10, loss, index, taxes) == [{'tax': 0.00}]

def test_sell_operation_with_tax_more_than_minimal():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 10000},{'operation': 'sell', 'unit-cost': 20, 'quantity': 10000}]
    current_total_quantity = 10000
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert sell_operation(operation_list, current_total_quantity, current_weighted_average_cost, 10000, 10, loss, index, taxes) == [{'tax': 0.00},{'tax': 20000.00}]

def test_calculate_operation_buy():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 10}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.00}]

def test_calculate_operation_sell_less_than_minimal():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 100},{'operation': 'sell', 'unit-cost': 10, 'quantity': 10}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.0}, {'tax': 0.0}]

def test_calculate_operation_sell_with_loss():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 100},{'operation': 'sell', 'unit-cost': 5, 'quantity': 10}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.0}, {'tax': 0.0}]

def test_calculate_operation_sell_with_profit_but_less_than_minimal():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 100},{'operation': 'sell', 'unit-cost': 20, 'quantity': 10}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.0}, {'tax': 0.0}]

def test_calculate_operation_sell_with_profit_and_more_than_minimal():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 10000},{'operation': 'sell', 'unit-cost': 20, 'quantity': 5000}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.0}, {'tax': 10000.0}]

def test_calculate_operation_sell_with_neutral():
    operation_list = [{'operation': 'buy', 'unit-cost': 10, 'quantity': 10000},{'operation': 'sell', 'unit-cost': 10, 'quantity': 5000}]
    current_total_quantity = 10
    current_weighted_average_cost = 10
    loss = 0
    index = 0
    taxes = ()
    assert calculate_operation(operation_list, current_total_quantity, current_weighted_average_cost, loss, index, taxes) == [{'tax': 0.0}, {'tax': 0.0}]

def test_get_weighted_average_cost_increase_value():
    current_total_quantity = 10
    current_weighted_average_cost = 10
    quantity = 10
    unitCost = 20
    assert get_weighted_average_cost(current_total_quantity, current_weighted_average_cost, quantity, unitCost) == 15

def test_get_weighted_average_cost_decrease_value():
    current_total_quantity = 10
    current_weighted_average_cost = 10
    quantity = 10
    unitCost = 5
    assert get_weighted_average_cost(current_total_quantity, current_weighted_average_cost, quantity, unitCost) == 7.5

def test_get_weighted_average_cost_maintain_value():
    current_total_quantity = 10
    current_weighted_average_cost = 10
    quantity = 10
    unitCost = 10
    assert get_weighted_average_cost(current_total_quantity, current_weighted_average_cost, quantity, unitCost) == 10

def test_get_loss_positive_value():
    current_weighted_average_cost = 20
    unitCost = 10
    quantity = 10
    loss = 0
    assert get_loss(current_weighted_average_cost, unitCost, quantity, loss) == 100

def test_get_loss_negative_value():
    current_weighted_average_cost = 10
    unitCost = 20
    quantity = 10
    loss = 0
    assert get_loss(current_weighted_average_cost, unitCost, quantity, loss) == -100

def test_get_loss_zero():
    current_weighted_average_cost = 10
    unitCost = 10
    quantity = 10
    loss = 0
    assert get_loss(current_weighted_average_cost, unitCost, quantity, loss) == 0

def test_is_less_or_equal_than_minimal_less():
    unitCost = 10
    quantity = 10
    assert is_less_or_equal_than_minimal(unitCost, quantity) == True

def test_is_less_or_equal_than_minimal_bigger():
    unitCost = 100
    quantity = 1000
    assert is_less_or_equal_than_minimal(unitCost, quantity) == False

def test_is_less_or_equal_than_minimal_equal():
    unitCost = 10
    quantity = 2000
    assert is_less_or_equal_than_minimal(unitCost, quantity) == True

def test_get_tax_over_profit_positive_value():
    unitCost = 20
    current_weighted_average_cost = 10
    quantity = 10
    loss = 0
    assert get_tax_over_profit(unitCost, current_weighted_average_cost, quantity, loss) == 20

def test_get_tax_over_profit_zero():
    unitCost = 10
    current_weighted_average_cost = 10
    quantity = 10
    loss = 0
    assert get_tax_over_profit(unitCost, current_weighted_average_cost, quantity, loss) == 0

def test_get_tax_over_profit_negative_value():
    unitCost = 10
    current_weighted_average_cost = 20
    quantity = 10
    loss = 0
    assert get_tax_over_profit(unitCost, current_weighted_average_cost, quantity, loss) == -20
