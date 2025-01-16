

# NOTE; budget = 120 
# exchange rate = 1.2 

def exchange_money(budget, exchange_rate):
    exchanged_currency = budget * exchange_rate
    return exchanged_currency

def get_change(budget, exchangeing_rate):
	return budget - exchangeing_rate

# Example usage
print(exchange_money(120, 1.2))  # Should print 144
print(get_change(120, 1.2))  # Should print 118.8

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
print(get_value_of_bills(20, 5))  # Should print 100
print(get_value_of_bills(50, 4))  # Should print 200

def get_number_of_bills(amount, denomination):
    return amount / denomination
print(get_number_of_bills(100, 20))  # Should print 5
print(get_number_of_bills(200, 50))  # Should print 4
print(exchange_money(120, 1.2))  # Should print 144
print(get_change(120, 1.2))  # Should print 118.8


def get_leftover_of_bills(amount, denomination):
    return get_leftover_of_bills(120, 1.2) == 20
print(get_leftover_of_bills(120, 1.2))  # Should print 20

def exchangeable_value(amount, exchange_rate, spread, denomination):
    return amount * exchange_rate * (1 - spread) / denomination