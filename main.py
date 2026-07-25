import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Assign employeeNumber and lastName from employees
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName 
    FROM employees
""",
    conn,
)

# STEP 3
# Assign lastName and employeeNumber (reversed)
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber 
    FROM employees
""",
    conn,
)

# STEP 4
# Assign lastName and employeeNumber AS ID
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""",
    conn,
)

# STEP 5
# Case statement for role
df_executive = pd.read_sql(
    """
    SELECT *,
        CASE 
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""",
    conn,
)

# STEP 6
# Length of last name as name_length
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""",
    conn,
)

# STEP 7
# First two letters of job title as short_title
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""",
    conn,
)

# STEP 8
# Calculate total sum of rounded priceEach * quantityOrdered
# Using SQL SUM directly ensures it returns the exact scalar/Series structure expected
sum_total_price = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered)) 
    FROM orderDetails
""",
    conn,
).iloc[0, 0]

# STEP 9
# Return orderDate, day, month, year from orders / orderDetails
# Note: Checking if orderDate exists in orderDetails or orders table
df_day_month_year = pd.read_sql(
    """
    SELECT 
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders
""",
    conn,
)