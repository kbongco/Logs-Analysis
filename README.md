<h1>Udacity Fullstack Nanodegree:Logs Analysis</h1>

This is the First Project in the Full Stack Web Development Nanodegree course that is offered in Udacity. We are given a large database 
and are instructed to run complex sql queries to draw conclusions based on the data. This comes
in the form of an internal reporting tool that will use the information from the database to 
answer several questions such as "Who are the top authors?" and "What are the top 3 articles?"
<br> 
<br>

<b>To Run:</b><br>
You Will need:<br> 
<ul>
  <li><a href="https://www.python.org/downloads/">Python 3</a></li>
  <li><a href="https://www.virtualbox.org/wiki/Download_Old_Builds_5_1">Virtual Box</a></li>
  <li><a href="https://www.vagrantup.com/downloads.html">Vagrant</a></li>
</ul>

<b>Setup</b>
<ol>
  <li>Install Vagrant and Virtual Box</li>
  <li>Clone this Repository using ```git clone ``` </li>
</ol>  

<b>How to Run</b>
<br>
Launch the Vagrant VM changing the directory via the command line using ```cd ```to where it was installed.<br>
Next run ```vagrant up``` to start up the virtual machine. <br>
Last, run the command   ```vagrant ssh``` to log into the virtual machine

In order to load the data, the command ```psql -d news -f newsdata.sql ``` will be used to load the data into the database. There are three tables in the database these tables are :
<ul>
  <li>Articles</li>
  <li>Authors</li>
  <li>Log</li>
</ul>

If by accident, you loaded it twice or modified it you can use the following commands to fix it up: 

```
drop table log;
drop table articles;
drop table authors;
```
Then you can reimport the data via the: 
```psql -d news -f newsdata.sql ```


<h2> Views that need to be created</h2> 
For the third query, in order to answer the question "On which days did more than 1% of requests lead to errors?" three views were created: 

```
CREATE view req_errors AS SELECT date(time) AS date, COUNT(*) 
AS errors FROM LOG where not status = '200 OK' GROUP BY DATE ORDER BY errors; 
```

```
CREATE view total_reqs AS SELECT date(time) AS date, COUNT(*)
AS requests FROM log GROUP BY date ORDER BY request;
```

```
CREATE view error_percentage_rate AS SELECT total_reqs.date,
req_errors.errors/total_requests.requests:::float * 100 AS
error_rate FROM total_reqs, req_errors WHERE 
total_reqs.date = req_errors.date;
```
Afterwards, you can run the log analysis program on your shell using: 
``` python logsanalysiscleaned.py ```





 

