# Logs Analysis Project
##### By: Sarah Thomens

## Project Description
This program accesses the news database provided by Udacity to answer three questions:
        1. What are the most popular three articles?
        2. Who are the most popular article authors?
        3. On which days did more than 1% of requests lead to errors?

 The program uses SQL commands to access the news database and javascript to
 create the readable output that answers the above three questions.

## How to Install and Run Project
1. Make sure you have the news database before running this project.
	* This is provided by the Udacity team [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Make sure you have created all views used by this code - all three views created for this project are listed below.
3. Run `python loganalysis.py` to run the project.


#### Views to Create Before Running Code:

1. `create view view_count as select path, count(path) as views from log where path like '%/article/%' group by path order by views desc;`
	* This creates a view called view_count with columns for path and views.
	* This view was created to count the number of times a path has been viewed in order to determine how many times an article has been viewed.
2. `create view article_info as select articles.title, authors.name as author, view_count.views from articles join view_count on concat('/article/', articles.slug) = view_count.path join authors on articles.author = authors.id order by view_count.views desc;`
	* This creates a view called article_info with columns for article title, author, and number of views of the article.
	* This view was created to have easy access to information about each article to help answer questions one and two of the project.
3. `create view request_data as select time::date as date, count(*) as total, sum(case when status like '%200%' then 1 else 0 end) as success, sum(case when not status like '%200%' then 1 else 0 end) as fail from log group by time::date order by time::date;`
	* This creates a view called request_data with columns for the date, total requests, total successes, and total fails.
	* This view was created to look at relevant request information of the database on each day the database was accessed to help answer question three of the project.
