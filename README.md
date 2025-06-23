# Task 1 : Data Cleaning
Task 1 - Data Cleaning

Work on : Netflix Movies and TV Shows  
Source: Kaggle - Netflix Titles (https://www.kaggle.com/datasets/shivamb/netflix-shows)

Objectives : 

The goal of this task was to clean and preprocess a real-world dataset by:

- Identifying and handling missing values
- Removing duplicate rows
- Standardizing text formats
- Fixing date formats and data types
- Cleaning column names

Tools Used
- Python 3
- Pandas library

Steps to perform a task :  

1. Removed rows with missing values in critical fields: date_added, rating and duration.
2. Filled missing values in director, cast, and country with "Unknown" value.
3. Removed duplicate rows while cleaning data.
4. Standardized text in type and country fields using .str.strip() and .str.title().
5. Converted date_added column to datetime format.
6. Renamed column headers to lowercase and replaced spaces with underscores.

Output
The cleaned dataset is saved as: netflix_titles_cleaned.csv 

Attached 3 files including 
- data_cleaning.py (which contains python(pandas) code to perform data cleaning.
- cleaned data named as netflix_titles_cleaned.csv
- Readme file to understand what I have done.

