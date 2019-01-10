import psycopg2

DBNAME = "news"

#Question 1: What are the top 3 most popular articles of all time?
Query1 = "SELECT articles.title, COUNT(*) as views FROM articles INNER JOIN log on log.path like CONCAT('%', articles.slug,'%') GROUP BY articles.title ORDER BY views DESC limit 3;"

#Question 2: Who are the most popular authors by view?
Query2 = "SELECT authors.name, COUNT(*) as views from articles INNER JOIN authors on articles.author = authors.id INNER JOIN log on log.path LIKE CONCAT('%', articles.slug,'%') WHERE log.status like '%200%' GROUP BY authors.name ORDER BY views DESC;"

#Question 3: What days did more than 1% requests lead to errors?
Query3 = "SELECT date, error_rate from error_percentage_rate where error_rate >=1;"


#Connect to the database
def connect():
    return psycopg2.connect("dbname=news")

#Print out the articles
def top_three_articles(Query1):
    db=connect()
    c=db.cursor()
    c.execute(Query1)
    results = c.fetchall()
    print('Top three articles by page view')
    for i in results:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
    print(" ")

#Print out authors
def popular_authors(Query2):
    db=connect()
    c=db.cursor()
    c.execute(Query2)
    results = c.fetchall()
    print('Most Popular authors of all time by view')
    for i in results:
          print(i[0] + ' -- ' + str(i[1]) + ' views')
    print('')

#Print out Error days
def error_days(Query3):
    db=connect()
    c=db.cursor()
    c.execute(Query3)
    results = c.fetchall()
    print('High error days when exceeding 1%')
    for result in results:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')


if __name__ == '__main__':
    print("Here are the results!")
    print("The Top three articles are:")
    top_three_articles(Query1)
    print("\n")
    print("The Top Authors are:")
    popular_authors(Query2)
    print("\n")
    print("High error days were on...")
    error_days(Query3)
    
    
        
