# Customer Purchase Pattern Analyzer
**PS No. 81 – Rungta International Skills University**

## About the Project

The Customer Purchase Pattern Analyzer is a menu-driven Python program that reads customer order data from `orders.csv` and turns it into useful insights. It shows how much customers spend each month, which month performs best, how spending is divided across product categories, and what a typical order value looks like using the mean and median. Results are displayed both as text output and as charts, so the data is easy to understand.

## Key Features

- **Monthly spending analysis:** Calculates total spending for each month and shows it in a chart.
- **Best month detection:** Automatically finds the month with the highest spending.
- **Order statistics:** Calculates the mean (average) and median (middle value) of order amounts.
- **Category share and statistics:** Shows what percentage of total spending each product category contributes, along with category-level statistics.
- **Visual output:** Uses Matplotlib charts to present results clearly.
- **Simple menu interface:** Easy to use, with numbered options and no complicated commands.

## Technologies Used

- **Python 3:** Main programming language
- **Pandas:** Reading the CSV file and grouping and analysing data
- **NumPy:** Numerical calculations
- **Matplotlib:** Creating charts and graphs

## Project Structure

```
Code/
├── main.py       # Main program file
└── orders.csv    # Customer orders dataset
```

## Requirements

- Python 3.x installed on your computer
- The following libraries: pandas, numpy, matplotlib

## How to Use

1. Install the required libraries:
   ```
   pip install pandas numpy matplotlib
   ```
2. Open the `Code` folder.
3. Run the program:
   ```
   python main.py
   ```

**Note:** `main.py` and `orders.csv` must be in the same folder, otherwise the program will not be able to find the data file.

## Menu Options

| Option | Name | What It Does |
|--------|------|--------------|
| 1 | Monthly spending | Shows total spending per month with a chart and the best month |
| 2 | Order statistics | Shows the mean and median order value |
| 3 | Category share and statistics | Shows each category's share of spending with a chart and statistics |
| 4 | Exit | Closes the program |

## Main Points

1. The program works with real order data from a CSV file, so the same code can be reused with other datasets in the same format.
2. Monthly analysis helps identify peak and low-sales periods, which is useful for planning offers and stock.
3. Comparing mean and median shows whether a few very large orders are affecting the average.
4. Category share shows which product categories bring in the most revenue.
5. The menu-based design lets the user choose only the analysis they need, without running everything at once.
6. Charts make the results easier to understand than raw numbers alone.

## Sample Results

Based on the analysed data:
- **Total spending:** Rs. 34,000 across 8 valid orders
- **Best month:** February (Rs. 12,500)

## Limitations

- The dataset is small, so the findings show general patterns rather than strong statistical conclusions.
- The program analyses spending only and does not include customer-level details such as age or location.

## Future Improvements

- Support larger datasets and different file formats.
- Add customer segmentation and repeat-purchase analysis.
- Build a dashboard or graphical interface.
- Add sales forecasting for upcoming months.

---

*PS No. 81 – Rungta International Skills University*

Agar chaho toh main isme "Sample Output" ya screenshots wala section bhi add kar sakta hoon, ya ise aur chhota bana sakta hoon.
