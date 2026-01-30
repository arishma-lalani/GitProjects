# Question 8

import pandas as pd

data = {
    "A": [1,2,2,1],
    "B": [3.1,4.2,1.5,6.3],
    "C": [800,150,400,210]
}

dataframe_of_column_data = pd.DataFrame(data)
dataframe_of_column_data["A_times_C"] = dataframe_of_column_data["A"] * dataframe_of_column_data["C"]
print(dataframe_of_column_data)