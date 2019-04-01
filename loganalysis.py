#!/usr/bin/env python

# =============================================================================
# Logs Analysis Project
# by: Sarah Thomens
#
# This program accesses the news database provided by Udacity to answer three
# questions:
#        1. What are the most popular three articles?
#        2. Who are the most popular article authors?
#        3. On which days did more than 1% of requests lead to errors?
#
# The program uses SQL commands to access the news database and javascript to
# create the readable output that answers the above three questions.
# =============================================================================

# -Import the PostgreSQL adaptor and the datetime module-----------------------
import psycopg2
import datetime

DBNAME = "news"    # Database name variable

# -Connecting to the news database and setting up the cursor-------------------
db = psycopg2.connect(database=DBNAME)
cursor = db.cursor()

# -----------------------------------------------------------------------------
# Question One: What are the most popular three articles?
#
# Executes the SQL command to create a table that includes the title and views
# of articles in a database limiting it to the top three articles using the
# article_info view. Saves results to articleRecords variable.
# -----------------------------------------------------------------------------
cursor.execute('''SELECT title,
                         views
               FROM article_info
               LIMIT 3;''')
articleRecords = cursor.fetchall()

# -----------------------------------------------------------------------------
# Question Two: Who are the most popular article authors?
#
# Executes the SQL command to create a table that includes the author and the
# sum of all their articles views using the article_info view and grouping by
# author name and ordering by number of views highest to lowest. Saves results
# to authorRecords variable.
# -----------------------------------------------------------------------------
cursor.execute('''SELECT author,
                         sum(views) AS views
               FROM article_info
               GROUP BY author
               ORDER BY views DESC;''')
authorRecords = cursor.fetchall()

# -----------------------------------------------------------------------------
# Question Three: On which days did more than 1% of requests lead to errors?
#
# Executes the SQL command to create a table that includes the date and the
# percentage of failed requests that are greater than 1% of requests on that
# day using the request_date view. Saves results to requestRecords variable.
# -----------------------------------------------------------------------------
cursor.execute('''SELECT TO_CHAR(date, 'Mon DD, YYYY'),
                         round(fail * 100.0 / total, 2) AS percentage
               FROM request_data
               WHERE (fail * 100.0 / total) > 1;''')
requestRecords = cursor.fetchall()
print(requestRecords)

# -Close the database----------------------------------------------------------
db.close()

# -Printing the results of all three questions---------------------------------
print("Top Three Articles")
print("------------------")
for x in articleRecords:
    print("  \"" + x[0] + "\"" + " - " + str(x[1]) + " views")

print("\nTop Three Authors")
print("-----------------")
for x in authorRecords:
    print("  " + x[0] + " - " + str(x[1]) + " views")

print("\nDays with More Than 1% Errors")
print("-----------------------------")
for x in requestRecords:
    print("  " + x[0] + " - " + str(x[1]) + "% errors")
