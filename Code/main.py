import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file="orders.csv"):
    """CSV padho aur galat Amount wali rows hata do."""
    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        return None

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")  # N/A -> NaN
    for i, amt in df["Amount"].items():
        if pd.isna(amt):
            print(f"Warning: Row {i + 1} skipped - Amount must be a number.")
        elif amt < 0:
            print(f"Warning: Row {i + 1} skipped - Amount cannot be negative.")

    df = df[df["Amount"] >= 0]  # sirf sahi rows bachti hain
    print(f"Valid orders analysed: {len(df)}")
    return df if len(df) else None


def fmt(x):
    """5000.0 ko 5000 dikhao, baaki ko 2 decimal tak."""
    return str(int(x)) if x == int(x) else f"{x:.2f}"


def monthly_totals(df):
    """Har month ka total (file ke order mein)."""
    return df.groupby("Month", sort=False)["Amount"].sum()


def print_mean_median(df):
    print(f"Mean order value: Rs. {np.mean(df['Amount']):.2f}")
    print(f"Median order value: Rs. {np.median(df['Amount']):.2f}")


def monthly_spending(df):
    totals = monthly_totals(df)
    for month, amt in totals.items():
        print(f"{month} : Rs. {fmt(amt)}")
    print(f"Total: Rs. {fmt(totals.sum())}")
    print(f"Best month: {totals.idxmax()} (Rs. {fmt(totals.max())})")

    totals.plot(kind="bar", color="skyblue", title="Monthly Spending")
    plt.ylabel("Amount (Rs.)")
    plt.tight_layout()
    plt.show()


def order_stats(df):
    totals = monthly_totals(df)
    print(f"Orders analysed: {len(df)}")
    print_mean_median(df)
    print(f"Best month: {totals.idxmax()} (Rs. {fmt(totals.max())})")


def category_share(df):
    totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    for cat, amt in totals.items():
        print(f"{cat} : Rs. {fmt(amt)} ({amt / totals.sum() * 100:.2f}%)")
    print_mean_median(df)

    plt.pie(totals, labels=totals.index, autopct="%1.2f%%")
    plt.title("Category Share")
    plt.show()


def main():
    df = load_data()
    if df is None:
        return

    menu = {"1": monthly_spending, "2": order_stats, "3": category_share}
    while True:
        print("\n1. Monthly spending")
        print("2. Order statistics")
        print("3. Category share and statistics")
        print("4. Exit")
        choice = input("Choose: ").strip()
        if choice == "4":
            break
        elif choice in menu:
            menu[choice](df)
        else:
            print("Invalid choice. Enter 1-4.")


main()