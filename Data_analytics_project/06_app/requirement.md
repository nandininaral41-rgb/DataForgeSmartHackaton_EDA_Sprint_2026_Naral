# Auto EDA Web App - Requirement Document

## Project Title
Auto EDA Tool (DataForge Sprint 2026)

---

## User
This application is designed for:
- Students
- Data Analysts
- Beginners in Data Science

---

## Problem Statement
Manual exploratory data analysis (EDA) is time-consuming and requires coding knowledge. Users need a simple tool that can quickly analyze any CSV file and provide instant insights.

---

## Input
- CSV file uploaded by the user
- Any structured dataset with rows and columns

---

## Output
The application provides:
- Dataset shape (rows and columns)
- Column names
- First 5 rows preview
- Interactive table view of data

---

## Features
- File upload system (CSV)
- Automatic dataset overview
- Data preview in tabular format
- Column detection
- Lightweight browser-based execution (no installation required)

---

## Success Criteria
The application is successful if:
- It accepts any valid CSV file
- It correctly displays dataset structure
- It shows sample data without errors
- It runs smoothly in a browser without backend setup

---

## Technology Used
- HTML
- JavaScript
- PapaParse library (for CSV parsing)

---

## Limitations
- No advanced charts in current version
- No backend data processing
- Large datasets may load slowly in browser

---

## Future Improvements
- Add charts using Chart.js
- Add missing value detection
- Add statistical summary (mean, median, etc.)
- Export analysis report as PDF