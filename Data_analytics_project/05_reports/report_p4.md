# Practical 4: Power BI Power Query Cleaning Pipeline

## Objective
To create a reusable ETL pipeline using Power BI Power Query for importing, cleaning, and transforming raw CSV data.

---

## Tools Used
- Power BI Desktop
- Power Query Editor
- CSV Dataset

---

## ETL Process

### 1. Extract
Imported the raw CSV file into Power BI using the Get Data option.

### 2. Transform
Performed data cleaning operations using Power Query:

- Promoted first row as headers
- Checked and corrected data types
- Removed data errors
- Created a conditional column (Order Size / Profit Status)
- Extracted Year from Date column
- Applied column transformations

### 3. Load
Used Close & Apply to load the cleaned dataset into Power BI.

---

# Report Questions

## Q1. How is Power Query different from manual Excel cleaning?

Power Query is an automated data transformation tool that records all cleaning steps as a reusable process. Manual Excel cleaning requires repeating the same steps every time new data arrives, while Power Query automatically applies the saved transformations.

---

## Q2. Which transformation would save time when new CSV data arrives?

Saved Power Query transformations save time because when a new CSV file with the same structure arrives, Power BI can refresh the data and automatically apply all previous cleaning steps.

---

## Conclusion

Power Query helps create an efficient ETL pipeline by automating data cleaning and transformation, making future data updates faster and more reliable.