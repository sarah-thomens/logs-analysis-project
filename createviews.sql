--------------------------------------------------------------------------------
-- This creates a view called view_count with columns for path and views.
-- It was created to count the number of times a path has been viewed in order
-- to determine how many times an article has been viewed.
--------------------------------------------------------------------------------
CREATE VIEW view_count AS
SELECT PATH,
       count(PATH) AS views
FROM log
WHERE PATH LIKE '%/article/%'
GROUP BY PATH
ORDER BY views DESC;

--------------------------------------------------------------------------------
-- This creates a view called article_info with columns for article title,
-- author, and number of views of the article.
-- This view was created to have easy access to information about each article
-- to help answer questions one and two of the project.
--------------------------------------------------------------------------------
CREATE VIEW article_info AS
SELECT articles.title,
       authors.name AS author,
       view_count.views
FROM articles
JOIN view_count ON concat('/article/', articles.slug) = view_count.path
JOIN authors ON articles.author = authors.id
ORDER BY view_count.views DESC;

--------------------------------------------------------------------------------
-- This creates a view called request_data with columns for the date, total
-- requests, total successes, and total fails.
-- This view was created to look at relevant request information of the
-- database on each day the database was accessed to help answer question
-- three of the project.
--------------------------------------------------------------------------------
CREATE VIEW request_data AS
SELECT TIME::date AS date,
       count(*) AS total,
       sum(CASE
               WHEN status LIKE '%200%' THEN 1
               ELSE 0
           END) AS success,
       sum(CASE
               WHEN NOT status LIKE '%200%' THEN 1
               ELSE 0
           END) AS fail
FROM log
GROUP BY TIME::date
ORDER BY TIME::date;
