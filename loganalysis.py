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


# -----------------------------------------------------------------------------
# Database Connection Function
#
# Connects to the PostgreSQL news database. Creates and returns a database
# connection. To use: db, cursor = connect(DBNAME).
# db, cursor: tuple
#     db: database connection
#     cursor: database cursor
# -----------------------------------------------------------------------------
def connect(database_name):
    # -Try to make a connection to the database--------------------------------
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor

    # -If no connection made, send an error to the terminal--------------------
    except psycopg2.Error as err:
        print "Unable to connect to database"
        print err
        sys.exit(1)


# -----------------------------------------------------------------------------
# Question One Function: What are the most popular three articles?
#
# Executes the SQL command to create a table that includes the title and views
# of articles in a database limiting it to the top three articles using the
# article_info view. Prints the formatted results to the terminal.
# -----------------------------------------------------------------------------
def questionOne(cursor):
    cursor.execute('''SELECT title,
                             views
                   FROM article_info
                   LIMIT 3;''')

    articleRecords = cursor.fetchall()    # article records variable

    # -Print the results-------------------------------------------------------
    print("Top Three Articles")
    print("------------------")
    for x in articleRecords:
        print("  \"" + x[0] + "\"" + " - " + str(x[1]) + " views")


# -----------------------------------------------------------------------------
# Question Two Function: Who are the most popular article authors?
#
# Executes the SQL command to create a table that includes the author and the
# sum of all their articles views using the article_info view and grouping by
# author name and ordering by number of views highest to lowest. Prints the
# formatted results to the terminal.
# -----------------------------------------------------------------------------
def questionTwo(cursor):
    cursor.execute('''SELECT author,
                             sum(views) AS views
                   FROM article_info
                   GROUP BY author
                   ORDER BY views DESC;''')

    authorRecords = cursor.fetchall()    # author records variable

    # -Print the results-------------------------------------------------------
    print("\nTop Three Authors")
    print("-----------------")
    for x in authorRecords:
        print("  " + x[0] + " - " + str(x[1]) + " views")


# -----------------------------------------------------------------------------
# Question Three Function: Which days did more than 1% of requests have errors?
#
# Executes the SQL command to create a table that includes the date and the
# percentage of failed requests that are greater than 1% of requests on that
# day using the request_date view. Prints the formatted results to the
# terminal.
# -----------------------------------------------------------------------------
def questionThree(cursor):
    cursor.execute('''SELECT TO_CHAR(date, 'Mon DD, YYYY'),
                             round(fail * 100.0 / total, 2) AS percentage
                   FROM request_data
                   WHERE (fail * 100.0 / total) > 1;''')

    requestRecords = cursor.fetchall()    # request records variable

    # -Print the results-------------------------------------------------------
    print("\nDays with More Than 1% Errors")
    print("-----------------------------")
    for x in requestRecords:
        print("  " + x[0] + " - " + str(x[1]) + "% errors")


# -----------------------------------------------------------------------------
# Program Run Function
#
# This function calls all other functions of the program and executes them to
# print out the results of all three questions listed above.
# -----------------------------------------------------------------------------
def run():
    # -Connect to the database-------------------------------------------------
    db, cursor = connect(DBNAME)

    # -Answer question one-----------------------------------------------------
    questionOne(cursor)

    # -Answer question two-----------------------------------------------------
    questionTwo(cursor)

    # -Answer question three---------------------------------------------------
    questionThree(cursor)

    # -Close the database------------------------------------------------------
    db.close()


if __name__ == '__main__':
    run()
else:
    print('Importing ...')
