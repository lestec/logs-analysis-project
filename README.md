# Logs Analysis Project
Logs Analysis project is the first project for the [Udacity Full Stack Web Developer Nanodegree Program.](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## About the project: 
We are given the following scenario:

```
You've been hired onto a team working on a newspaper site. 
The user-facing newspaper site frontend itself, and the database behind it, are already built and
running. You've been asked to build an internal reporting tool that will use information from the 
database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. 
The log has a database row for each time a reader loaded a web page. Using that information, your code 
will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the 
user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out 
the answers to some questions.

```
---
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

What is the reporting tool reporting?
	The reporting tool is going to answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
---

# How to Run the Program

## Setting up the project

1.  Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) 
	    to install and manage virtual machine to create an enviroment to run the project.   
	
2.  Download the VM configuration zip file by [Udacity](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip)
	    OR Clone the repository from [here](https://github.com/udacity/fullstack-nanodegree-vm)
	
3.  Clone this repo (my github) to the vagrant folder that is inside  
	    the VM configuration file that was downloaded/cloned above.  
	
4.  Once the project has been setup, navigate into the project directory
	    with 'Vagrantfile' and then `cd logs-analysis-project`

## Run the Program
	
5.  Start the virtual machine with `vagrant up`
	
6.  Connect to the virtual machine with `vagrant ssh`
	
7.  Go to the folder where the guest/host files are shared `cd /vagrant`
	
8.  Unzip the news database `unzip /newsdata.sql` or to download zip file https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
	
9.  To load the database type `psql -d news -f newsdata.sql`
	
10. To connect to the database type `psql -d news`
	
11. Now you must run the commands from the Views section below to
		to run the python program successfully. 
    
12. After adding the views to exit out of news database type `\q`
    
13. Then `cd logs-analysis-project/`
    
14. To run the python program that fetches the query results use
    command `python scripts/logs_analysis.py` the output is written in the terminal.   

## Create the following VIEWS (step #11 from above) for question #3

```
CREATE VIEW all_errors AS
SELECT time::date as date, count (*) as errors 
FROM log 
WHERE status != '200 OK' 
GROUP BY date;

```

```
CREATE VIEW daily_views AS
SELECT time::date as date, count (*) as views 
FROM log 
GROUP BY date;

```

```
CREATE VIEW daily_error_percent AS
select to_char(daily_views.date, 'MM DD, YYYY') as date, round(100.0 * all_errors.errors/daily_views.views, 2) as percentage from daily_views, all_errors where daily_views.date = all_errors.date order by
daily_views.date;

```
# Troubleshooting
If your command prompt does not start with vagrant after typing `vagrant ssh` then please try the `winpty vagrant ssh` on your Windows system.

# Resource Links
[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

pycodestyle \
https://pycodestyle.readthedocs.io/en/latest/intro.html \
https://www.python.org/dev/peps/pep-0008/

PostgreSQL documentaion \
https://www.postgresql.org/docs/current/index.html

Installing Vagrant on Ubuntu \
https://howtoprogram.xyz/2016/07/23/install-vagrant-ubuntu-16-04/
