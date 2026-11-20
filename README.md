# Customer Purchase Pattern Analyzer

**Name:** KUNAL SONBARSA
**Class/Section:** M
**ERP:** RU-26-01559
**PS No.:** 81
**University:** Rungta International Skills University

---

## Project Description

This program reads the `orders.csv` file and analyzes customer purchase patterns. It includes the following features:

- Monthly spending (with charts)
- Best month (the month with the highest spending)
- Category share (how much was spent in each category)
- Mean and median order value
- Invalid rows (text or negative Amount) are skipped with a warning

## Libraries Required

- pandas
- numpy
- matplotlib

To install them:

```bash
pip install pandas numpy matplotlib
```

## Steps to Run

1. Install the libraries above (`pip install pandas numpy matplotlib`).
2. Open the project code folder.
3. Run the following command in the Terminal/Command Prompt:

```bash
python main.py
```

> **Note:** `main.py` and `orders.csv` must be in the same folder.

## Menu Options

1. Monthly spending
2. Order statistics
3. Category share and statistics
4. Exit

## Sample Input (`orders.csv`)

```
OrderID,Month,Category,Amount
1,Jan,Grocery,2000
2,Jan,Clothing,3000
3,Feb,Grocery,2500
4,Feb,Electronics,10000
5,Mar,Grocery,3000
6,Mar,Clothing,2000
7,Apr,Electronics,8000
8,Apr,Grocery,3500
```

## Sample Output

**Option 1: Monthly spending**

```
Valid orders analysed: 8
Jan : Rs. 5000
Feb : Rs. 12500
Mar : Rs. 5000
Apr : Rs. 11500
Total: Rs. 34000
Best month: Feb (Rs. 12500)
```

**Option 3: Category share and statistics**

```
Electronics : Rs. 18000 (52.94%)
Grocery : Rs. 11000 (32.35%)
Clothing : Rs. 5000 (14.71%)
Mean order value: Rs. 4250.00
Median order value: Rs. 3000.00
```

**Invalid rows (Amount = N/A and Amount = -500)**

```
Warning: Row 9 skipped - Amount must be a number.
Warning: Row 10 skipped - Amount cannot be negative.
Valid orders analysed: 8
```
