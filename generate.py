import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

def generate_random_transaction_data(output_file: str, num_rows: int = 100):
    """
        What this does?
        It generates random transaction data and saves it to an Excel file.

        How?
        - It generates random transaction data using the random and datetime modules.
        - It creates a DataFrame from the generated data using pandas.
        - It saves the DataFrame to an Excel file using the to_excel method.
    """
    # Generate random transaction data
    data = []
    for _ in range(num_rows):
        transaction_id = str(uuid.uuid4())  # Unique transaction ID
        date = datetime.now() - timedelta(days=random.randint(1, 365))  # Random date in the past year
        amount = round(random.uniform(10, 1000), 2)  # Random amount between $10 and $1000
        category = random.choice(["Groceries", "Electronics", "Clothing", "Entertainment", "Food", "Others"])
        payment_method = random.choice(["Credit Card", "Debit Card", "Cash", "UPI", "Wallet"])
        status = random.choice(["Success", "Failed", "Pending"])
        
        data.append({
            "Transaction ID": transaction_id,
            "Date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "Amount": amount,
            "Category": category,
            "Payment Method": payment_method,
            "Status": status,
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Random transaction data saved to {output_file}")

# Example Usage
generate_random_transaction_data("random_transactions.xlsx", num_rows=100000)