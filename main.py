import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas (Done above)

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employeeNumber and lastName from employees
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName 
    FROM employees
""",
    conn,
)

# STEP 3
# Select lastName before employeeNumber
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber 
    FROM employees
""",
    conn,
)

# STEP 4
# Select lastName, employeeNumber aliased as 'ID'
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""",
    conn,
)

# STEP 5
# Use CASE to bin jobTitle into 'Executive' or 'Not Executive' as 'role'
df_executive = pd.read_sql(
    """
    SELECT *,
        CASE 
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""",
    conn,
)

# STEP 6
# Length of last name as 'name_length'
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""",
    conn,
)

# STEP 7
# First two letters of job title as 'short_title'
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""",
    conn,
)

# STEP 8
# Total price = ROUND(priceEach * quantityOrdered), then sum
# Note: In SQLite, standard strftime('%d'), strftime('%m'), strftime('%Y') are used for dates,
# but for Step 8 we sum the rounded total prices:
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""",
    conn,
).sum()

# STEP 9
# Return orderDate followed by day, month, and year extracted from orderDate
df_day_month_year = pd.read_sql(
    """
    SELECT 
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orderDetails
""",
    conn,
)

conn.close()