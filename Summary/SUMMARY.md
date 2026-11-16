# Customer Purchase Pattern Analyzer
**PS No. 81 – Rungta International Skills University**

## Project Overview

The Customer Purchase Pattern Analyzer is a data analysis project that studies customer buying behaviour using order records stored in `orders.csv`. It cleans the raw data and turns it into clear insights through statistics and visualisations. The aim is to help a business understand when customers spend the most, what a typical order looks like, and which product categories contribute the most to revenue.

## Objectives

- Load and clean customer order data from a CSV file.
- Analyse how spending changes month by month.
- Calculate order statistics (mean and median) to understand typical order values.
- Show category-wise spending share using charts.
- Present the findings in an easy-to-read, visual format.

## Main Features

- **Monthly spending analysis:** Groups orders by month and shows total spending per month in a chart, making peak and low periods easy to spot.
- **Order statistics:** Calculates the mean (average) and median (middle value) of order amounts, giving both the overall average and a typical order value that is not distorted by very large or very small orders.
- **Category-wise share:** Shows how total spending is divided among product categories, so the most popular and most profitable categories are clearly visible.
- **Data validation:** Only valid orders are included, which keeps the results reliable.

## Key Results

- **Total spending analysed:** Rs. 34,000
- **Valid orders:** 8
- **Average order value (mean):** Rs. 4,250 (Rs. 34,000 ÷ 8)
- **Best month:** February, with spending of Rs. 12,500, which is roughly 37% of the total spending

## Main Points / Key Insights

1. February was the strongest month, contributing more than a third of total spending.
2. The average order value is about Rs. 4,250, which gives a baseline for pricing and sales targets.
3. Comparing mean and median shows whether a few large orders are pushing the average up.
4. Category-wise charts show which categories drive most of the revenue, helping with stock and marketing decisions.
5. Monthly trends can guide promotions, for example running offers in weaker months to balance sales.

## Problems Faced During Development

1. **Invalid or dirty data:** Some rows had missing values, negative amounts, or wrong formats. These were filtered out, which is why only 8 valid orders were analysed.
2. **Inconsistent date formats:** Dates appeared in different formats, which broke the monthly grouping. They had to be standardised, for example with `pandas.to_datetime()`.
3. **Mean skewed by outliers:** A few large orders could inflate the average, so the median was added to represent a typical order more fairly.
4. **Small dataset:** With only 8 valid orders, the trends are hard to generalise and the charts show limited patterns.
5. **Chart readability:** With few categories and values, pie chart labels overlapped, so label formatting and figure size had to be adjusted.
6. **Duplicate entries:** Repeated orders risked double-counting spending, so duplicates were removed.
7. **File handling errors:** Wrong file paths or encoding issues caused read errors such as `FileNotFoundError`, which were fixed by correcting the path and setting `encoding='utf-8'`.

## Limitations

- The dataset is very small, so the conclusions are indicative rather than statistically strong.
- The analysis covers spending only, with no customer demographics or repeat-purchase behaviour.

## Future Scope

- Use a larger, real-world dataset for more reliable patterns.
- Add customer segmentation and repeat-customer analysis.
- Build an interactive dashboard (for example with Streamlit or Power BI).
- Add forecasting to predict future monthly spending.

## Conclusion

The project shows how raw order data can be cleaned and turned into useful business insights. Even with a small dataset, it identifies the best-performing month, the typical order value, and the category-wise revenue split, which are the foundation for better sales planning.

---

**Note:** The "Problems Faced" section is based on typical issues in data analysis projects, not on what actually happened in your project. Please check each point and replace or remove any that don't match your experience, so the report stays honest if your teacher asks about it. If you tell me the actual problems (specific errors, library issues, etc.), I can rewrite that section accordingly.
