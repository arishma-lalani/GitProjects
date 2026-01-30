# Question 3

def calculate_the_power(base, exponent):
    return base ** exponent

list_of_base_and_exponent_pairs = [[5,2], [3,-1], [4,3], [2,0]]

valid_results_of_power_calculations = []

for base_number, exponent_value in list_of_base_and_exponent_pairs:
    if exponent_value < 0:
        continue
    results_of_power_calculation = calculate_the_power(base_number, exponent_value)
    valid_results_of_power_calculations.append(results_of_power_calculation)
print(valid_results_of_power_calculations)