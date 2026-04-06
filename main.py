import pandas as pd
import matplotlib.pyplot as pit

#Csv file
df = pd.read_csv("transactions.csv")
#data
print("=== Transaction Data ===")
print(df)

#Total spending 
total_spent = df["Amount"].sum()
print("\nTotal Spending : $", total_spent)

#spending by category

category_spending = df.groupby("Category")["Amount"].sum()
print("\nSpending by category:")
print(category_spending)


#Rule set up Amount > 1000 is suspicious 
print("n\=== Suspicious Transactions ===")
#Rule set up Amount > 1000 is suspicious 
suspicious = df[df["Amount"]>1000]
print(suspicious)


# Plot spending by category
import matplotlib.pyplot as plt
category_spending.plot(kind='bar')
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()