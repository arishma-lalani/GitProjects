# Question 2

def nested_dictionary(list_of_strings):
    resulting_dictionary = {}
    for string in list_of_strings:
        length_of_the_string = len(string)
        if length_of_the_string % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        resulting_dictionary[string] = {"length": length_of_the_string, "parity": parity}

    return resulting_dictionary

strings = ["data", "science"]
print(nested_dictionary(strings))