#!/usr/bin/python

import cgi,cgitb,pymysql
form=cgi.FieldStorage()
c_shuming=form.getvalue('shuming')
connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("insert into book(shuming,no) values('%s',0);" %(c_shuming))
print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "</head>"
print "<body>"
print "<p>we have gotten your suggestion</p>"
print "<body/>"
print "<html/>"