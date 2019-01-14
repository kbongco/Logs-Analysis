import psycopg2

DBNAME = "news"

#Question 1: What are the top 3 most popular articles of all time?
Query1 = "SELECT articles.title, COUNT(*) as views FROM articles INNER JOIN log on log.path like CONCAT('/article/', articles.slug) GROUP BY articles.title ORDER BY views DESC limit 3;"

#Question 2: Who are the most popular authors by view?
Query2 = "SELECT authors.name, COUNT(*) as views from articles INNER JOIN authors on articles.author = authors.id INNER JOIN log on log.path LIKE CONCAT('/article/', articles.slug) WHERE log.status = '200 OK' GROUP BY authors.name ORDER BY views DESC;"

#Question 3: What days did more than 1% requests lead to errors?
Query3 = "SELECT date, percent from error_percentage_rate where percent >=1;"


#Connect to the database
def connect():
    return psycopg2.connect("dbname=news")

#Print out the articles
def top_three_articles(Query1):
    db=connect()
    c=db.cursor()
    c.execute(Query1)
    results = c.fetchall()
    for x in results:
        print('"' + x[0] + '" have ' + str(x[1]) + " views")

#Print out authors
def popular_authors(Query2):
    db=connect()
    c=db.cursor()
    c.execute(Query2)
    results = c.fetchall()
    for x in results:
          print(x[0] + ' had ' + str(x[1]) + ' views')

#Print out Error days
def error_days(Query3):
    db=connect()
    c=db.cursor()
    c.execute(Query3)
    results = c.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' at ' + str(result[1]) + ' %')

print("Here are the results!")
print("\n")
print("The Top three articles by page view are:")
top_three_articles(Query1)
print("\n")
print("The Top Authors are:")
popular_authors(Query2)
print("\n")
print("High error days exceeding 1% were on:")
error_days(Query3)
    
    
        
