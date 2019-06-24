#! /usr/bin/env python

# import Postgresql library
import psycopg2

# global database name
DBNAME = "news"


# Query 1: What are most popular 3 articles of all time?
def popular_three_articles():
    # Connect to database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Execute queries
    c.execute("""
        SELECT articles.title, count(*) as num
        FROM articles
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
        """)
    # fetch results
    results = c.fetchall()
    db.close()
    print "\n\n--- Three most popular articles of all time ---"
    for article in results:
        print "%s -- %s views" % (article[0], article[1])


# Query 2: Who are the most popular article authors of all time?
def popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT authors.name, count(*) as num
        FROM authors, articles, log
        WHERE authors.id = articles.author
        AND log.path = concat('/article/', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
        """)
    results = c.fetchall()
    db.close()
    print "\n\n--- Most popular authors of all time ---"
    for author in results:
        print "%s -- %s views" % (author[0], author[1])


# Query 3: On which days did more than 1% of request lead to errors?
def days_most_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        SELECT *
        FROM daily_error_percent
        WHERE daily_error_percent.percentage >1
        ORDER BY daily_error_percent.percentage DESC;
        """)
    result = c.fetchall()
    db.close()
    print "\n\n--- Days with more than 1 percent of request lead to errors ---"
    for error in result:
        print "%s - %s%%" % (error[0], error[1])


if __name__ == '__main__':
    popular_three_articles()
    popular_authors()
    days_most_errors()
