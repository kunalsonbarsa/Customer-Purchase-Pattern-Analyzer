# Customer Purchase Pattern Analyzer

**Name:** KUNAL SONBARSA
**Class/Section:** M
**ERP:** RU-26-01559
**PS No.:** 81
**University:** Rungta International Skills University

---

## Project Overview

This project analyzes customer purchase data from the `orders.csv` file. Built with Python, Pandas, NumPy and Matplotlib, it provides a simple menu-driven program that shows:

- **Monthly spending**, displayed as a chart
- **Best month**, the month with the highest spending
- **Order statistics**, including the mean and median order value
- **Category-wise share**, displayed as a chart

**Key results from the sample data:**

- Total spending analyzed: Rs. 34,000 across 8 valid orders
- Best month: February (Rs. 12,500)

## Difficulties Faced and How I Solved Them

**1. Invalid or messy data in the CSV file**
Some rows had missing or incorrect values, which caused errors and wrong totals.
*Solution:* I cleaned the data with Pandas before the analysis, dropping invalid rows and converting columns to the correct types. This is why only the 8 valid orders are counted.

**2. Grouping spending by month**
Dates were read as plain text, so they could not be grouped by month directly.
*Solution:* I converted the date column to a proper datetime format and then grouped by month to get monthly totals and the best month.

**3. Choosing between mean and median**
A few very high or very low orders made the mean misleading.
*Solution:* I showed both the mean and the median, so the typical order value is clearer.

**4. Making the charts readable**
The first charts had overlapping labels and unclear category shares.
*Solution:* I adjusted the labels, titles and figure size in Matplotlib so the charts are easy to read.

**5. File path errors while running the program**
The program failed when `orders.csv` was not in the same folder as `main.py`.
*Solution:* I kept both files in the same folder and documented this requirement in the README.

## Conclusion

The project gave me hands-on practice in data cleaning, analysis and visualization with Python, and in handling real-world problems such as invalid data and unclear charts.
