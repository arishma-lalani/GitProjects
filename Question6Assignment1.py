# Question 6

def calculate_distribution_percentage_of_list(list_of_numbers_given):
    length_of_list_of_numbers = len(list_of_numbers_given)
    cumulative_distribution_dictionary = {}
    unique_values_in_given_list = []
    for number in list_of_numbers_given:
        if number not in unique_values_in_given_list:
            unique_values_in_given_list.append(number)
    unique_values_in_given_list.sort()
    for unique_value in unique_values_in_given_list:
        count_of_elements_less_than_or_equal_to_the_value = 0
        for number in list_of_numbers_given:
            if number <= unique_value:
                count_of_elements_less_than_or_equal_to_the_value = count_of_elements_less_than_or_equal_to_the_value + 1
        percent_less_than_or_equal = (count_of_elements_less_than_or_equal_to_the_value / length_of_list_of_numbers) * 100
        cumulative_distribution_dictionary[unique_value] = percent_less_than_or_equal

    return cumulative_distribution_dictionary

numbers_list = [3,1,2,3,4,2]
print(calculate_distribution_percentage_of_list(numbers_list))