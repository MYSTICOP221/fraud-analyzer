import pandas as pd
import matplotlib.pyplot as plt


# Loading transactions

try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    print("transactions.csv not found in current folder")
    exit()

print("=== Transaction Data ===")
print(df)


# Analysis phase
total_spent = df["Amount"].sum()
print(f"\nTotal spending: $ {total_spent}")

category_spending = df.groupby("Category")["Amount"].sum()
print("\nSpending by Category:")
print(category_spending)


# Fraud Detection
print("\n=== Suspicious Transactions ===")

# Rule 1: Dynamic threshold (mean + 2*std deviation)
threshold = df["Amount"].mean() + 2 * df["Amount"].std()
suspicious_high = df[df["Amount"] > threshold]

# Rule 2: Rapid transactions (same category on same day >1)
rapid_transactions = df.groupby(["Date", "Category"]).filter(lambda x: len(x) > 1)

# Combine suspicious transactions
suspicious_combined = pd.concat([suspicious_high, rapid_transactions]).drop_duplicates()

if suspicious_combined.empty:
    print("No suspicious transactions found")
else:
    print(suspicious_combined)

# Visualization

category_spending.plot(kind='bar', color='skyblue')
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# Exporting

export_choice = input("Do you want to export suspicious transactions to CSV? (y/n): ")
if export_choice.lower() == 'y':
    suspicious_combined.to_csv("suspicious_transactions.csv", index=False)
    print("Suspicious transactions exported to suspicious_transactions.csv")