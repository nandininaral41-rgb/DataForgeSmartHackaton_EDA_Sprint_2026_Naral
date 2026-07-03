# Practical 5: DAX Measures and KPI Creation in Power BI

## Objective
To create calculated measures using DAX (Data Analysis Expressions) in Power BI and visualize key business KPIs for decision making.

---

## Dataset Used
The dataset contains sales-related data including:
- Sales Amount
- Profit
- Order ID
- Discount
- Quantity

---

## What is DAX?
DAX (Data Analysis Expressions) is a formula language used in Power BI to create:
- Calculated columns
- Measures
- KPI calculations

It helps in performing dynamic calculations based on filters and visuals.

---

## Difference Between Column and Measure

| Feature | Column | Measure |
|--------|--------|---------|
| Calculation | Row-by-row | Aggregated result |
| Storage | Stored in table | Not stored |
| Performance | Slower for large data | Faster |
| Usage | Static values | Dynamic KPIs |

---

## Created Measures (DAX)

- Total Sales = SUM(Sales[Sales Amount])
- Total Profit = SUM(Sales[Profit])
- Order Count = COUNT(Sales[Order ID])
- Average Discount = AVERAGE(Sales[Discount])
- Profit Margin = DIVIDE([Total Profit], [Total Sales], 0)

---

## KPI Design Decision

The most important KPI placed at the top of dashboard is:

### 👉 Total Sales

Because:
- It represents overall business performance
- It is the base for Profit and Profit Margin
- It is the most commonly tracked business metric

---

## Insights from KPIs

- Sales performance shows overall revenue trend
- Profit indicates business efficiency
- Discount helps understand pricing strategy
- Profit Margin shows business health

---

## Conclusion
DAX measures help convert raw data into meaningful business insights. KPI cards allow quick decision-making and executive-level understanding of performance.

---

## Output
A Power BI dashboard with KPI cards and DAX measures successfully created.