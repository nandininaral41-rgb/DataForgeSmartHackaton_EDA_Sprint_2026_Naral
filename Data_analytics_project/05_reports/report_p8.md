# Practical 8: Python Cleaning, Type Conversion and Feature Engineering

## Objective
To clean the dataset using Python, perform feature engineering, and create a reusable cleaning script for reproducible data processing.

## Cleaning Steps Performed
- Loaded the dataset using the Pandas library.
- Checked for duplicate records and removed them if present.
- Checked for missing values in all columns.
- No missing values were found in the dataset, so no imputation was required.
- Converted the date column to datetime format (if available).
- Extracted **Month** and **Year** from the date column.
- Exported the cleaned dataset as `dataforge_cleaned.csv`.

## Data Wrangling
- Grouped the data by **Region**.
- Calculated the average **Sales** for each region.
- Exported the aggregated data as `region_sales_aggregated.csv`.

## Report Questions

### 1. What cleaning decision could affect business conclusions?

Removing duplicate records and handling missing values can significantly affect business conclusions because these steps influence totals, averages, trends, and overall data accuracy.

### 2. Which engineered feature is most useful and why?

The **Month** and **Year** features are the most useful because they enable time-based analysis, making it easier to identify seasonal trends and compare business performance over different periods.

## Conclusion

The dataset was successfully cleaned and transformed using Python. Data quality was verified, useful features were created, regional sales aggregation was performed, and the cleaned dataset was exported for further analysis.