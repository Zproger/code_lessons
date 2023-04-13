

""" Связывание for else и except """

data_strings = ["1", "2", "3"]
parsed_data = []

for data_str in data_strings:
    try:
        value = int(data_str)
        parsed_data.append(value)
    except ValueError:
        print(f"Error parsing string '{data_str}'")
        break
else:
    print("Job completed.")

