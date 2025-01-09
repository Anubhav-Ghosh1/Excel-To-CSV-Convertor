# Excel to CSV Convertor

# What this does?
    It takes an Excel file as input, reads the specified sheet, and converts it to a CSV file.

# How it does?
    - It uses the openpyxl library to read the Excel file.
    - It reads the specified sheet using the sheet_name parameter.
    - It converts the sheet data to a DataFrame using pandas.
    - It saves the DataFrame to a CSV file using the to_csv method.

# How to run?
    1. Data generation
    ```
        python generate.py
    ```
    2. Excel to CSV Convertor
    ```
        python main.py
    ```